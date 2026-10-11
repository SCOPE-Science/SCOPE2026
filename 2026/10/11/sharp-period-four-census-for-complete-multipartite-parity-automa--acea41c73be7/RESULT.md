# Sharp period-four census for complete multipartite parity automata

## Finding

Consider the complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\) and every \(n_i\ge1\). Put \(N=\sum_i n_i\), let \(k=\#\{i:n_i\text{ is odd}\}\), and let \(e=r-k\). On the Boolean state space \(\mathbb F_2^N\), let \(A\) be the graph adjacency operator reduced modulo two. The self-exclusive and self-inclusive parity updates are, respectively, \(F_0(x)=Ax\) and \(F_1(x)=(I+A)x\).

Define three nonnegative integers
\[
\begin{split}
a_1&=r-\mathbf1_{\{r\text{ odd}\}},\\
a_2&=k-\mathbf1_{\{k\text{ odd and }e=0\}},\\
a_3&=k-\mathbf1_{\{k\text{ odd}\}}.
\end{split}
\]
For \(j\in\{0,1\}\), let \(P_{j,d}=\#\operatorname{Fix}(F_j^d)\). Then the *exact* counts for every choice of positive part sizes are
\[
\begin{array}{c|ccc}
&d=1&d=2&d=4\\ \hline
j=0&2^{u}&2^{a_3}&2^{a_3}\\
j=1&2^{N-a_1}&2^{N-a_2}&2^{N-a_3}
\end{array},
\qquad
u=\begin{cases}0,&k=0,\\k-1,&k\ge1.\end{cases}
\]
There are no primitive periodic orbits of any other length. For either update, the number of cycles of exact lengths \(1,2,4\), respectively, is
\[
C_{j,1}=P_{j,1},\qquad
C_{j,2}=\frac{P_{j,2}-P_{j,1}}2,\qquad
C_{j,4}=\frac{P_{j,4}-P_{j,2}}4.
\]
Consequently the Artin--Mazur dynamical zeta function, defined by \(\zeta_{F_j}(z)=\exp(\sum_{m\ge1}\#\operatorname{Fix}(F_j^m)z^m/m)\), is the rational function
\[
\zeta_{F_j}(z)=(1-z)^{-C_{j,1}}(1-z^2)^{-C_{j,2}}(1-z^4)^{-C_{j,4}}.
\]

In particular, \(F_0\) has a genuine two-cycle if and only if \(k\) is a positive even integer, while \(F_1\) has a genuine four-cycle if and only if \(k\) is odd and \(e\ge1\). The bounds are uniform in \(N\): every \(F_0\)-trajectory enters a cycle of period at most two in at most three updates, and every \(F_1\)-trajectory enters a cycle of period at most four in at most two updates. The maximum period four is attained already on \(K_{1,2}\).

## Assumptions and scope

All algebra is over \(\mathbb F_2\), with synchronous updates, no added constant bit, and no self-loops in the graph. The two values of \(j\) denote exclusively the presence or absence of the self-state in the XOR update. The graph is undirected, complete between distinct nonempty parts, and empty within every part. Fixed-point counts are counts of distinct *global configurations* fixed by the specified iterate, not counts of spatially homogeneous states. The zeta identity is a formal-power-series identity and hence also a rational-function identity. No large-system limit is assumed.

## Proof

**1. Reduction to part parities.** Let \(s:\mathbb F_2^N\to\mathbb F_2^r\) send a configuration to its vector of part parities, and let \(E:\mathbb F_2^r\to\mathbb F_2^N\) duplicate each component over its part. These maps are surjective and injective, respectively. Write \(\mathbf1\) for the all-ones column of length \(r\), \(C=I_r+\mathbf1\mathbf1^{\mathsf T}\), and \(D=\operatorname{diag}(n_1\bmod2,\ldots,n_r\bmod2)\). Directly from the neighborhood XOR rule,
\[
A=ECs,\qquad sE=D,\qquad A^2=ECDCs.
\]
The kernel of \(C\) is zero for even \(r\), and is the line spanned by \(\mathbf1\) for odd \(r\). Therefore \(\operatorname{rank}A=a_1\).

**2. Rank at two steps.** Order the \(k\) odd-sized parts before the \(e\) even-sized parts and write \(J_{ab}=\mathbf1_a\mathbf1_b^{\mathsf T}\). Matrix multiplication over \(\mathbb F_2\) gives
\[
CDC=\begin{cases}
\begin{pmatrix}I_k&J_{ke}\\J_{ek}&0\end{pmatrix},&k\text{ even},\\[5pt]
\begin{pmatrix}I_k+J_{kk}&0\\0&J_{ee}\end{pmatrix},&k\text{ odd}.
\end{cases}
\]
For even \(k\), the first matrix has rank \(k\), since the Schur complement of \(I_k\) vanishes by \(J_{ek}J_{ke}=kJ_{ee}=0\). For odd \(k\), \(I_k+J_{kk}\) has rank \(k-1\), while \(J_{ee}\) has rank one exactly when \(e>0\). Thus \(\operatorname{rank}A^2=a_2\). The same formulas apply when a block has dimension zero, interpreted as an empty matrix.

**3. Stable image and finite-power identities.** On any part-constant configuration, the next values on the odd parts are \(Hc\), where \(H=I_k+J_{kk}\), and those on the even parts are all the parity \(\sum_{i\text{ odd}}c_i\). If \(k\) is even, \(H^2=I_k\); if \(k\) is odd, \(H^2=H\) and the components of \(Hc\) have even total parity. Accordingly,
\[
\begin{array}{c|c|c}
&\operatorname{rank}A^3&\text{identity}\\\hline
k\text{ even}&k&A^4=A^2\\
k\text{ odd}&k-1&A^4=A^3.
\end{array}
\]
These identities also follow directly by applying the preceding odd/even-coordinate update twice. Thus \(a_3=\operatorname{rank}A^3\), and \(A^4\) has rank \(a_3\). The eventual invertible image of \(A\) has dimension \(a_3\): there it is an involution for even \(k\), and the identity for odd \(k\). When \(k\) is even and positive, its fixed subspace has dimension \(k-1\), since \(Hc=c\) is equivalent to \(\sum c_i=0\). When \(k\) is odd the entire eventual image, of dimension \(k-1\), is fixed. When \(k=0\), only zero is periodic. This establishes the entire first row of the displayed fixed-point table, including \(P_{0,4}=P_{0,2}\).

**4. Inclusion of the self-state.** Over \(\mathbb F_2\), \((I+A)^2=I+A^2\) and \((I+A)^4=I+A^4\). Hence
\[
\operatorname{Fix}(F_1)=\ker A,\quad
\operatorname{Fix}(F_1^2)=\ker A^2,\quad
\operatorname{Fix}(F_1^4)=\ker A^4.
\]
Using the computed ranks gives the second table row. If \(k\) is even, \((I+A)^4=(I+A)^2\). If \(k\) is odd, \(A^4=A^3\) implies \(A^5=A^4\), so the characteristic-two binomial identity \((I+A)^5=I+A+A^4+A^5=I+A\) gives \(F_1^5=F_1\). These global identities bound the transient and all cycle lengths; they also justify the enumeration of every possible prime period. Counting each primitive cycle \(d\) times in \(\#\operatorname{Fix}(F_j^d)\) yields the displayed cycle counts and zeta function.

**5. Sharpness and a real-spectrum contrast.** On \(K_{1,2}\), \((P_{1,1},P_{1,2},P_{1,4})=(2,4,8)\), so there are precisely two fixed points, one two-cycle and one four-cycle. For every \(m\ge1\), the graph \(K_{2m,2m}\) has \(k=0\). Therefore \(A^2=0\) and \((I+A)^2=I\) even though the ordinary real adjacency spectral radius is \(2m\), which is unbounded as \(m\to\infty\). The real-Jacobian growth diagnostic and the eventual finite Boolean cycle structure are mathematically different invariants; neither is being equated with the other.

## Verification

Run `python verify.py` with Python 3 and its standard library. It constructs all \(427\) ordered complete multipartite examples having between two and six parts, each of size one to three, and at most ten vertices. Every state is exhaustively enumerated for each such graph. The program checks ranks of the first three adjacency powers, the characteristic-two power identities, the counts of configurations fixed by the first, second, and fourth iterates for both parity updates, and integral primitive-cycle formulas. This produces the exact diagnostic `VERIFY_OK graphs= 427  assertions= 481628`. Finite checking supports the indexing, not the universal theorem; Steps 1--5 provide the proof for all admissible \(N,r,n_i\).

## Relationship to prior work

Rollier and Baetens (2026) rigorously identify the real-valued Boolean-Jacobian Lyapunov spectrum for the network parity rule with the real graph-adjacency spectrum; their Section 4 also explicitly separates real tangent-space growth from true modulo-two defects. Their paper does not give the complete multipartite period counts, period-four criterion, or zeta function established here. General linear finite dynamical systems and Fitting decompositions are classical. Kantic, Qureshi, Panario, and Legl (2026) give algorithms for cycle lengths and tree heights in cyclic-module linear finite dynamical systems over Galois rings, but not the parity-by-part-size closed-form classification of these graph updates. The new result should be understood as an explicit structural calculation within, not an alternative to, finite-field linear dynamical systems theory.

## Limitations

The classification is specific to complete multipartite simple graphs and to the two unshifted parity rules, and it does not cover arbitrary graphs, nonbinary state sets, asynchronous updates, or affine additions of a constant bit. It does not say real Lyapunov exponents are erroneous: they concern real tangent-space matrix growth, not the finite Boolean orbit count. Originality remains subject to the possibility of an equivalent earlier finite-field network calculation, even if not found in the sources inspected.

## References

1. M. Rollier and J. M. Baetens, *Exact Lyapunov spectra of affine cellular automata and the parity rule on networks*, arXiv:2606.14521v1 (first submitted 12 June 2026), especially Sections 2.3, 4.1, 4.2 and 4.4.
2. J. Kantic, C. Qureshi, D. Panario and F. Legl, *On the Dynamics of Linear Finite Dynamical Systems Over Galois Rings*, arXiv:2604.01548v1 (2 April 2026), Sections 2--5.
3. R. A. Hernández-Toledo, *Linear finite dynamical systems*, Communications in Algebra 33 (2005), 2977--2989.
4. D. Bollman and O. Colón-Reyes, *Determining steady state behaviour of discrete monomial dynamical systems*, Advances in Mathematics of Communications 11 (2017), 283--287.
