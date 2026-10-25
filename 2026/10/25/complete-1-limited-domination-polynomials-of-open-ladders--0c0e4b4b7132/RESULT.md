# Complete 1-limited-domination polynomials of open ladders

## Finding

Let \(L_n=P_n\square K_2\) be the open two-row ladder with \(n\ge1\) labeled rungs. A vertex subset \(D\subseteq V(L_n)\) is **1-limited dominating** when every vertex outside \(D\) has a neighbor in \(D\), while every vertex in \(D\) has **at most one** neighbor outside \(D\). Write
\[
\mathcal L_n(z)=\sum_{D\text{ 1-limited dominating in }L_n}z^{|D|}.
\]
Then the entire cardinality distribution is specified, for every \(n\ge1\), by
\[
\boxed{\sum_{n\ge1}\mathcal L_n(z)t^n=\frac{zt\,B(t,z)}{Q(t,z)}},
\]
where
\[
\begin{aligned}
B(t,z)={}&(z+2)+(2z^2+4z)t+(z^4+3z^3+2z^2)t^2\\
&+(z^5+2z^4+4z^3)t^3+2z^5t^4,\\
Q(t,z)={}&1-z^2t-z^3t^2-(z^5+2z^4)t^3\\
&-(z^6+z^5+z^4)t^4-z^6t^5.
\end{aligned}
\]
In particular, the 1-limited-domination number is \(\gamma_1^{\mathrm L}(L_n)=n\). The number of minimum 1-limited dominating sets is \(2\) when \(n\) is odd and \(4\) when \(n\) is even. Every minimum set is one of the two full rows, or, when \(n\) is even, one of the two alternating runs of paired full and empty columns, with columns \(00,11,11,00,00,11,11,00,\ldots\) and its bitwise complement.

The total numbers of 1-limited dominating subsets, beginning at \(n=1\), are
\[
3,9,18,43,99,226,517,1187,2722,6237,14297,32778,\ldots.
\]
All vertices are distinguished; no quotient by graph automorphisms is taken.

## Assumptions and scope

Graphs are finite, undirected, and simple; \(P_n\) is the \(n\)-vertex path. The case \(n=1\) is \(L_1=K_2\). In a column, bits \(a_0,a_1\in\{0,1\}\) indicate which two vertices belong to \(D\). Identical set configurations related by reflection or row exchange are counted separately when the subsets differ. The variable \(z\) marks the number of selected vertices, and \(t\) marks the number of columns. The formal generating function lies in \(\mathbb Z[z][[t]]\).

## Proof

**Step 1: exact local tests.** Encode a column by \(a\in\{0,1,2,3\}\), with \(a_r=\lfloor a/2^r\rfloor\bmod2\), and write \(w(a)=a_0+a_1\). For a selected vertex (bit \(1\)), its adjacent bits must contain at most one \(0\); for an unselected vertex (bit \(0\)), they must contain at least one \(1\). Define \(E(a,b)\in\{0,1\}\) by applying these two conditions in both rows to the column \(a\) with its rung neighbor and its sole horizontal neighbor in column \(b\). Likewise, define \(I(a,b,c)\) by applying them to both vertices of the middle column \(b\), using the rung neighbor and the corresponding vertices in columns \(a,c\). These are Boolean tests on at most three bits at a time; `verify.py` gives their literal definitions.

**Step 2: 16-state transfer matrix.** Index matrix rows and columns by ordered pairs \((a,b)\in\{0,1,2,3\}^2\). Set
\[
T_{(a,b),(d,c)}=\mathbf1_{d=b}\,I(a,b,c)\,z^{w(c)},\quad
u_{(a,b)}=E(a,b)z^{w(a)+w(b)},\quad
v_{(a,b)}=E(b,a).
\]
Then direct identification of each interior and boundary column gives the exact identity
\[
\mathcal L_1(z)=2z+z^2,\qquad
\mathcal L_n(z)=u^{\mathsf T}T^{n-2}v\quad(n\ge2).
\]
Every choice of \(n\) column states occurs in this product exactly once, with weight \(z^{|D|}\). The local tests are necessary and sufficient because the definition depends only on immediate neighbors.

**Step 3: exact finite polynomial certificate for the rational identity.** Introduce
\[
R(X;z)=X^5-z^2X^4-z^3X^3-(z^5+2z^4)X^2
 -(z^6+z^5+z^4)X-z^6.
\]
The checker constructs the above 16-state transfer exactly over \(\mathbb Z[z]\), and verifies the following **sixteen polynomial identities**, coefficient by coefficient:
\[
u^{\mathsf T}T^jR(T;z)v=0\qquad(0\le j\le15).
\]
Because \(T\) is a \(16\times16\) matrix over a commutative ring, Cayley--Hamilton gives a monic polynomial identity of degree \(16\) for \(T\). Consequently, each \(T^j\) for \(j\ge16\) is an \(\mathbb Z[z]\)-linear combination of \(I,T,\ldots,T^{15}\). Thus the displayed equalities hold for every \(j\ge0\). Rewriting them via Step 2 gives, for every \(n\ge7\),
\[
\begin{aligned}
\mathcal L_n={}&z^2\mathcal L_{n-1}+z^3\mathcal L_{n-2}
+(z^5+2z^4)\mathcal L_{n-3}\\
&+(z^6+z^5+z^4)\mathcal L_{n-4}+z^6\mathcal L_{n-5}.
\end{aligned}
\]
Here all polynomials have argument \(z\). Direct exact transfer calculation verifies the same recurrence at \(n=6\) and verifies that the first five coefficients of \(Q(t,z)\sum_{n\ge1}\mathcal L_n(z)t^n\) are the coefficients of \(ztB(t,z)\). Therefore the claimed generating-function identity holds as an equality of formal power series for all \(n\).

This is a finite algebraic certificate for an infinite identity, **not** an inference from experimental agreement at finitely many graph sizes. The exact operations and all sixteen tested identities can be reproduced with the bundled standard-library checker.

**Step 4: minimum sets.** The domination requirement gives at least one cross-boundary edge from each vertex outside \(D\), while the 1-limited requirement gives at most one such edge from each vertex in \(D\). Hence \(|V\setminus D|\le|D|\), yielding \(|D|\ge n\). Selecting a full horizontal row meets the requirements, so the minimum is exactly \(n\).

Equality forces every vertex, on either side of the cut \((D,V\setminus D)\), to have **exactly one** neighbor across the cut. If one rung contains exactly one selected vertex, its rung edge is already the unique cut edge at both endpoints; neither can change membership across a horizontal edge. Induction along the connected row paths forces every rung to have the identical singleton pattern. This yields precisely the two full rows.

Otherwise each rung is monochromatic, of type \(00\) or \(11\). Write its common bit as \(s_i\). The rung edge does not cross the cut. For each vertex to have exactly one crossing horizontal edge, the binary transition indicators \(e_i=\mathbf1_{s_i\ne s_{i+1}}\) must satisfy \(e_1=e_{n-1}=1\) and \(e_{i-1}+e_i=1\) for \(2\le i\le n-1\). They consequently alternate \(1,0,1,0,\ldots\), satisfying the right endpoint condition exactly when \(n\) is even. The initial bit has two choices, yielding exactly the two asserted alternating column configurations. The \(n=1\) case has the two singleton minima. This completes the minimum-set classification.

## Verification

Execute `python3 verify.py` from a directory containing the bundled checker. It requires only the Python standard library. It independently reconstructs every ladder adjacency list, enumerates all selected/unselected vertex subsets for \(1\le n\le9\), tests the local transfer formulation, and checks the proposed minimum-set patterns. Separately, it checks all formal polynomial coefficients needed for the sixteen finite matrix identities and the initial rational numerator, using exact integer polynomial dictionaries. The expected final line is `VERIFY_OK`; the included `verify_output.txt` records the actual output. In particular, direct small-order agreement alone is not used to justify the unbounded range.

## Relationship to prior work

Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1 (first publicly submitted June 21, 2026), establishes the exact value \(\gamma_1^{\mathrm L}(P_m\square P_n)=mn/2\) when at least one path order is even, which implies \(\gamma_1^{\mathrm L}(L_n)=n\). The minimum **value** is therefore prior work. The paper's grid section addresses minimum sizes and structural bounds, not this all-cardinality polynomial or the full list of minimum sets.

Božović, Radić, Kovijanić-Vukićević and Tepeh, *On k-limited domination in graphs*, DOI:10.1007/s40314-026-03902-2, develops the definition, general bounds, and links to \((1,t)\)-domination and to \((0,k)\)-pitchfork domination, without supplying the ladder polynomial. Ordinary ladder domination polynomials and total-domination counts concern weaker or different conditions and do not enumerate the present constrained subset family. The complete refined rational series, including every cardinality coefficient, is the result claimed here. A literature search cannot exclude unindexed equivalent work.

## Limitations

The result concerns **open** two-row ladders only; it does not assert a corresponding formula for circular ladders, wider grids, or arbitrary graph products. It counts selected vertex sets, not automorphism classes. The minimum value was known previously. The rational-function proof uses a small, fully reproduced exact integer-polynomial certificate plus Cayley--Hamilton, rather than a closed-form characterization of every nonminimum set. Independent mathematical validation has not been performed, and earlier unindexed equivalent enumerations may exist.

## References

1. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1, 2026-06-21, https://arxiv.org/abs/2606.22428.
2. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On k-limited domination in graphs*, Computational and Applied Mathematics, DOI:10.1007/s40314-026-03902-2, https://link.springer.com/article/10.1007/s40314-026-03902-2.
3. OEIS A303054, *Number of minimum total dominating sets in the n-ladder graph*, https://oeis.org/A303054 (different domination condition).
4. OEIS A347558, *Number of minimum dominating sets in the n-ladder graph*, https://oeis.org/A347558 (ordinary domination condition).
