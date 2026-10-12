# Exact subalgebra permutability in the four-dimensional filiform Lie algebra

## Finding
For every prime power \(q\ge 2\), let \(L_q\) be the four-dimensional Lie algebra over \(\mathbb F_q\) with ordered basis \(x,y,z,w\) and the only nonzero basis brackets, up to alternating bilinearity,
\[
[x,y]=z,\qquad [x,z]=w.
\]
Write \(\mathcal L(L_q)\) for its **entire** subalgebra lattice, including the zero subalgebra and \(L_q\) itself. Two subalgebras \(A,B\) are **permutable** when \(A+B\) is a Lie subalgebra, equivalently \([A,B]\subseteq A+B\). Their subalgebra commutativity degree is the proportion of ordered permutable pairs.

The complete count is
\[
\boxed{|\mathcal L(L_q)|=q^3+3q^2+3q+5},
\qquad
\boxed{\#\{(A,B):[A,B]\not\subseteq A+B\}=q^3(q^3+6q^2+4q+1)}.
\]
Consequently,
\[
\boxed{
\operatorname{sd}(L_q)=\frac{11q^4+27q^3+39q^2+30q+25}{(q^3+3q^2+3q+5)^2}.
}
\]
In particular, \(\operatorname{sd}(L_q)\sim 11/q^2\) and tends to zero as \(q\to\infty\), along **all** prime powers. This includes characteristic two and nonprime finite fields.

## Assumptions and scope
The field \(\mathbb F_q\) is finite, with no restriction on characteristic. The bracket above is alternating, even in characteristic two, and satisfies Jacobi: the span \(D=\langle z,w\rangle\) is abelian, while \(\operatorname{ad}_x\) sends \(y\) to \(z\), \(z\) to \(w\), and \(w\) to zero. Thus \(L_q\) is the standard filiform nilpotent Lie algebra of dimension four and nilpotency class three. The invariant counts **subalgebra** permutability, not commuting element pairs, comaximal generation, or all modular pairs.

For clarity, use the following distinct subalgebra families, where parameters independently range over \(\mathbb F_q\). They describe actual subspaces, not merely isomorphism types.

* Four central/derived-subspace families: \(Z_0=0\); \(Z_c=\langle w\rangle\); \(Z_t=\langle z+t w\rangle\), for \(t\in\mathbb F_q\); and \(Z_2=\langle z,w\rangle=D\). The \(Z_t\) family has \(q\) members.
* Three families projecting onto a line with nonzero \(x\)-component:
  \[
  X_0(b,c,d)=\langle x+b y+c z+d w\rangle,\quad
  X_1(b,c)=\langle x+b y+c z,w\rangle,\quad
  X_2(b)=\langle x+b y,z,w\rangle.
  \]
  Their numbers are, respectively, \(q^3,q^2,q\).
* Three families projecting onto the line \(\langle y+D\rangle\):
  \[
  Y_0(c,d)=\langle y+c z+d w\rangle,\quad
  Y_{1,c}(c)=\langle y+c z,w\rangle,\quad
  Y_{1,t}(t,d)=\langle y+d w,z+t w\rangle,
  \]
  together with \(Y_2=\langle y,z,w\rangle\). The respective numbers are \(q^2,q,q^2,1\). Put \(Y_1=Y_{1,c}\sqcup Y_{1,t}\), so \(|Y_1|=q^2+q\).
* The full algebra \(L_q\).

Here \(X_i,Y_i,Z_i\) are labels for **families**; for example \(X_0\) denotes all \(X_0(b,c,d)\). These families are disjoint and exhaust the subalgebras.

## Proof
**Step 1: exhaustive subalgebra classification.** Let \(\pi:L_q\to L_q/D\cong\mathbb F_q^2\) be the quotient map. For a subalgebra \(A\), put \(U=\pi(A)\) and \(W=A\cap D\). If \(\dim U=0\), \(A\) is any subspace of the abelian plane \(D\), giving \(Z_0,Z_c,Z_t,Z_2\).

If \(\dim U=1\) and its generator is \(x+b y+D\), then \([x+b y,z]=w\). Thus the only \(\operatorname{ad}_{x+b y}\)-stable subspaces of \(D\) are \(0\), \(\langle w\rangle\), and \(D\). Choosing a lift modulo \(W\) gives exactly \(X_0,X_1,X_2\). If instead \(U=\langle y+D\rangle\), then \([y,D]=0\), so every subspace \(W\le D\) occurs, giving exactly the \(Y\)-families above.

If \(\dim U=2\), generators projecting to \(x+D,y+D\) have a bracket of the form \(z+\alpha w\), so \(W\) contains a noncentral vector. Bracketing that vector with a lift of \(x+D\) gives \(w\in W\). Hence \(W=D\) and \(A=L_q\). This proves completeness without a characteristic assumption. Summing the sizes of the displayed families gives
\[
(q+3)+(q^3+q^2+q)+(q^2+(q^2+q)+1)+1
=q^3+3q^2+3q+5.
\]

**Step 2: cross-bracket test.** If \(v=(a,b,c,d)\) and \(u=(a',b',c',d')\) are their coordinates in the ordered basis, then
\[
[v,u]=(ab'-ba')z+(ac'-ca')w.
\]
Because each listed family is closed under brackets, the sum \(A+B\) is a subalgebra if and only if every cross-bracket of its displayed generators lies in that vector-space sum. This is a finite system of span tests, rather than an inference from numerical interpolation.

**Step 3: exhaustive failure table.** Up to reversing the ordered pair, the **only** failures occur for the following pairs of families. The table gives the number for one ordered orientation, except where the two families coincide.

| Families | Failure condition | Number |
| --- | --- | ---: |
| \(X_0,X_0\) | Different projection slopes, or equal slopes with different \(z\)-coefficients | \(q^4(q^2-1)\) |
| \(X_0,X_1\) | Different projection slopes | \(q^4(q-1)\) |
| \(X_1,X_1\) | Different projection slopes | \(q^3(q-1)\) |
| \(X_0,Y_0\) | Always | \(q^5\) |
| \(X_0,Y_1\) | Always | \(q^4(q+1)\) |
| \(X_1,Y_0\) | Always | \(q^4\) |
| \(X_1,Y_1\) | Exactly when the \(Y_1\)-member contains \(\langle w\rangle\) | \(q^3\) |
| \(X_0,Z_t\) | Always, for each of the \(q\) noncentral lines \(Z_t\) | \(q^4\) |

For the first row, distinct slopes contribute \(q^5(q-1)\) failures: the two generators project independently to \(L_q/D\) but bracket nontrivially into \(D\). Equal slopes and unequal \(z\)-coefficients contribute \(q^4(q-1)\) further failures: the vertical intersection of the span is a line with nonzero \(z\)-component, while their cross-bracket is a nonzero multiple of \(w\), which is outside that line. These add to \(q^4(q^2-1)\).

For \(X_0\) against \(X_1\), and for \(X_1\) against \(X_1\), different projection slopes leave only \(\langle w\rangle\) inside the sum in the derived plane, although the bracket has a nonzero \(z\)-component. Equal slopes are permutable because the sum contains any needed \(z\)-direction, or the cross-brackets vanish.

Every \(X_0\)--\(Y_0\) and \(X_1\)--\(Y_0\) pair has independent quotient projections and an uncaptured \(z\)-component. Every \(X_0\)--\(Y_1\) pair fails: when \(Y_1\) contains \(w\) its cross-bracket has a nonzero \(z\)-component, and otherwise the bracket with its noncentral vertical generator produces \(w\) outside the vertical intersection. For \(X_1\)--\(Y_1\), the failure occurs precisely in the \(q\)-member \(Y_{1,c}\) family; with \(Y_{1,t}\), the two vertical lines \(\langle w\rangle\) and \(\langle z+t w\rangle\) span \(D\), making the pair permutable. Finally, \([x+b y+c z+d w,z+t w]=w\notin X_0(b,c,d)+Z_t\).

No other pair fails: members of the \(Y\)-families commute with one another and with all subspaces of \(D\); \(Z_0,Z_c,Z_2\) are permutable with every listed family (as appropriate by centrality or by closure of the span); each \(X_2\), \(Y_2\), and \(L_q\) contains the derived plane or is an ideal, so its sum with any other subalgebra is closed; and \(X_1\) with a \(Z_t\) spans the entire derived plane. This exhausts the table.

**Step 4: sum.** The two off-diagonal orientations contribute twice their displayed table values; the two diagonal rows contribute once. The ordered nonpermutable-pair total therefore equals
\[
\begin{aligned}
N_q={}&q^4(q^2-1)+2q^4(q-1)+q^3(q-1)\\
&+2q^5+2q^4(q+1)+2q^4+2q^3+2q^4\\
={}&q^3(q^3+6q^2+4q+1).
\end{aligned}
\]
By the definition of subalgebra commutativity degree,
\[
\operatorname{sd}(L_q)=1-\frac{N_q}{(q^3+3q^2+3q+5)^2}
=\frac{11q^4+27q^3+39q^2+30q+25}{(q^3+3q^2+3q+5)^2}.
\]
The leading terms in numerator and denominator have degrees four and six, giving the asserted \(11/q^2\) asymptotic and limit zero.

## Verification
The accompanying `verify.py` independently generates **every** subspace of \(\mathbb F_q^4\) by reduced-row-echelon matrices, tests Lie closure using the defining bracket, and then tests every ordered pair of subalgebras by direct cross-bracket rank computations. It separately checks all entries of the failure table, not only the final total.

The following exhaustive runs completed successfully:

| Field order | Total subalgebras | Nonpermutable ordered pairs | Permutable ordered pairs |
| ---: | ---: | ---: | ---: |
| \(2\) | \(31\) | \(328\) | \(633\) |
| \(3\) | \(68\) | \(2538\) | \(2086\) |
| \(4\) | \(129\) | \(11328\) | \(5313\) |
| \(5\) | \(220\) | \(37000\) | \(11400\) |
| \(7\) | \(516\) | \(228438\) | \(37818\) |

The \(q=4\) instance is implemented over \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) rather than an integer residue ring. Reproduce with `python3 verify.py`; the final line is `VERIFY_OK`. These experiments corroborate, but do not establish, the universal theorem, which follows from the exhaustive symbolic family and cross-bracket arguments above.

## Relationship to prior work
Muhie, Otera and Russo (arXiv:2609.19086v1, 2026-09-16) define the invariant and compute it for the three-dimensional Heisenberg Lie algebra, while proving comparisons and bounds for broader classes. Their Theorems 1.2--1.4 concern the Heisenberg case, a three-dimensional simple case, and Lazard correspondence; no four-dimensional filiform count occurs in their inspected text.

The August 2026 work of Towers, Zuleta and Gutierrez (arXiv:2608.16575v1) studies **comaximal generation graphs**, including a four-dimensional filiform algebra. This is a nearby object but an inequivalent invariant: a pair can have a proper nonclosed vector sum and nevertheless generate the full algebra. Its full text was unavailable for inspection, so one cannot exclude additional unpublished-in-abstract overlap; only its abstract and secondary summary were accessible.

Other published calculations of subalgebra commutativity degree concern five-dimensional and higher Heisenberg Lie algebras, the four-dimensional **central stabilization** of the three-dimensional Heisenberg algebra, and dimension-three Lie algebras. None of those stated theorems contains this class-three filiform algebra as a case. The central stabilization has limiting degree \(1/4\), whereas the present four-dimensional class-three algebra has limit zero; the comparison isolates a marked change caused by noncentral nilpotent structure, not by dimension alone. Published work on filiform **element** commutativity degrees computes \(\#\{(u,v):[u,v]=0\}\) instead of permutability of subalgebras and does not imply the new subalgebra-pair census.

A potential bridge remains via subgroup commutativity degrees of finite maximal-class \(p\)-groups, by Lazard correspondence when the characteristic exceeds the nilpotency class. Dedicated queries did not identify an equivalent previously published formula. Absence from those searches is not proof of historical uniqueness.

## Limitations
This is a classification for the single natural four-dimensional standard filiform algebra over each finite field, not for arbitrary class-three Lie algebras, deformed filiform algebras, or all four-dimensional solvable Lie algebras. The count is for ordered pairs and includes both the zero and whole subalgebras. No statement is made about the number of nonpermutable **modular** pairs, and the formula does not determine comaximal-graph invariants. The most material originality risk is an older equivalent subgroup-lattice calculation, or a related result hidden in the inaccessible complete four-dimensional filiform comaximal-graph article. The result has not received independent validation.

## References
1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, first publicly posted 2026-09-16.
2. D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1, posted 2026-08-17. This is a distinct invariant; complete-text comparison remains unresolved.
3. M. Tărnăuceanu, *The subgroup commutativity degree of finite P-groups*, arXiv:1312.0296, and *Bulletin of the Australian Mathematical Society* 93 (2016), 37–41. General group-side background, not an equivalent computation established here.
