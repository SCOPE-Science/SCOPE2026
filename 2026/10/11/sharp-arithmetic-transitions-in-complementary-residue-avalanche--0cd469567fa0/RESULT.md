# Sharp arithmetic transitions in complementary residue avalanche complexes
## Finding
Consider simultaneous sandpile firing on a consistently oriented finite directed cycle. When the binary support is one ordinary congruence class, taken **inside a finite linearly indexed interval** rather than as a coset of a subgroup of the cyclic vertex group, its translates can wrap across the class boundaries. The resulting avalanche homotopy types exhibit the following exact arithmetic transition.

**Theorem.** Let \(k\ge2\), \(n=kq+s\), \(q\ge2\), \(1\le s<k\), and \(\gcd(s,k)=1\). For each \(a\in\{0,\ldots,k-1\}\), put
\[
R_a=\{j\in\{0,\ldots,n-1\}: j\equiv a\pmod{k}\},\quad
\delta_a=\begin{cases}1,&a<s,\\0,&a\ge s,\end{cases}\quad L_a=q+\delta_a.
\]
Write \(\mathcal A(C_n,\mathbf1_S)\) for the avalanche simplicial complex obtained from the initial binary configuration supported on \(S\). Then
\[
\mathcal A(C_n,\mathbf1_{R_a})\simeq S^1.
\]
For the complementary configuration define \(T_a=q+s-(1+\delta_a)(k-1)\). The following precise alternatives hold:
\[
\mathcal A(C_n,\mathbf1_{R_a^c})\simeq
\begin{cases}
S^{2k-3},&T_a>0,\\
\bigvee^{L_a} S^{2k-4},&T_a=0.
\end{cases}
\]
The theorem does not assert either formula when \(T_a<0\).

In particular, if \(q+s>2(k-1)\), every residue \(a\) gives a circle for the supported configuration and a sphere \(S^{2k-3}\) for its complement. This is a systematic failure, on an infinite family of cycle lengths, of the unrestricted assertions printed as Lemma 3.17 and Conjecture 3.18 in Riihimäki--Smith (2026). At the boundary \((n,k)=(8,3)\), complementary zero-support positions \(a=0,1\) yield \(\bigvee^3S^2\), while \(a=2\) yields \(S^3\). The difference between congruence classes at the same \((n,k)\) is an arithmetic phase change.

## Assumptions and scope
The graph \(C_n\) is the directed cycle with vertices \(\mathbb Z/n\mathbb Z\) and exactly one edge \(j\to j+1\) per vertex. A vertex with at least one grain fires in the simultaneous round, losing one grain and sending one grain to its successor. For the initial binary configuration \(\mathbf1_S\), all configurations remain binary and the nonzero support moves by one cyclic step per round. The avalanche complex contains every face of every set of vertices firing in a common round. The coprimality assumption concerns \(n\) and \(k\), not the residue representatives. Homotopy equivalence is of ordinary geometric realizations, and integral homology is understood unless coefficients are specified.

The quotient/remainder notation is literal: \(n=kq+s\) with \(q\ge2\) and \(1\le s<k\). Both \(R_a\) and \(R_a^c\) have at least two vertices; the theorem makes no claim about noncoprime periods or about configurations with multiplicities greater than one.

## Proof
**1. Exact firing orbit.** Let \(c^{(t)}_j\in\{0,1\}\). At one parallel firing round, every occupied vertex loses a grain and each successor receives the grain from its predecessor, so \(c^{(t+1)}_j=c^{(t)}_{j-1}\). Therefore the fired-vertex sets are exactly \(S+t\) for \(t\in\mathbb Z/n\mathbb Z\), and the avalanche complex is the union of the full simplices on those translated sets. This also proves that no transient firing faces are omitted.

**2. Modular interval identification.** Since \(\gcd(k,n)=\gcd(s,k)=1\), multiplication of all vertex labels by \(u=k^{-1}\pmod n\) is a permutation. The congruence-class support \(R_a\) has \(L_a=q+\delta_a\) elements, in the order \(a,a+k,\ldots,a+(L_a-1)k\). Its image under multiplication by \(u\) is an interval of exactly \(L_a\) consecutive residues modulo \(n\). Every translated support \(R_a+t\) becomes a translate of the same interval, because multiplication by \(u\) permutes the \(n\) translation parameters. The complement becomes a complementary circular interval of length \(n-L_a\). Consequently the two avalanche complexes are, **as abstract simplicial complexes**, respectively
\[
\mathcal A(C_n,\mathbf1_{R_a})\cong\mathcal N(n,L_a-1),\qquad
\mathcal A(C_n,\mathbf1_{R_a^c})\cong\mathcal N(n,n-L_a-1).
\]
Here \(\mathcal N(n,r)\) denotes the complex with facets the length-\(r+1\) cyclic intervals in \(\mathbb Z/n\mathbb Z\), as in Adamaszek--Adams--Frick--Peterson--Previte-Johnson, Definition 3.2.

**3. The supported configuration.** Since \(q\ge2\), we have \(L_a-1\ge1\). Also \(L_a-1\le q<n/2\), because \(k\ge2\) and \(s\ge1\). Thus \(1\le L_a-1<n/2\). The circle case of the circular-arc nerve theorem implies \(\mathcal N(n,L_a-1)\simeq S^1\).

**4. The complementary configuration and the exact transition.** Put \(r=n-L_a-1\). First \(0\le r\le n-2\), as both parts of the support have at least two vertices. We claim
\[
\frac r n<\frac{k-1}{k},\qquad
\frac r n\begin{cases}>\frac{k-2}{k-1},&T_a>0,\\=\frac{k-2}{k-1},&T_a=0.\end{cases}
\]
For the first inequality, \(r/n<(k-1)/k\) is equivalent to \(L_a+1>n/k\), which holds since \(L_a+1\ge q+1>q+s/k=n/k\). The second inequality, after multiplying positive denominators, is equivalent to \(L_a+1<n/(k-1)\), respectively equality. With \(L_a=q+\delta_a\), this is exactly \((1+\delta_a)(k-1)<q+s\), respectively equality. Therefore the parameter lies in the open \(\ell=k-2\) odd-sphere interval of the circular-arc nerve theorem when \(T_a>0\), and on its lower endpoint when \(T_a=0\). Theorem 3.6 of Adamaszek et al. gives, respectively, \(S^{2\ell+1}=S^{2k-3}\) or a wedge of \(n-r-1=L_a\) spheres of dimension \(2\ell=2k-4\). This proves the theorem.

**5. Sharp uniform boundary and the source's assertions.** If \(q+s>2(k-1)\), both \(\delta_a=0\) and \(\delta_a=1\) make \(T_a>0\), hence the asserted uniform pair of types. When \(q+s=2(k-1)\), the classes with \(a<s\) give \(T_a=0\), whereas the classes with \(a\ge s\) have \(T_a=k-1>0\). These outcomes have different reduced homology degrees, so the strict inequality is sharp for a uniform complementary \(S^{2k-3}\) conclusion. For \((n,k)=(8,3)\), \(q=2,s=2\), so the first two classes have \(L_a=3,T_a=0\) and the third has \(L_a=2,T_a=2\).

Finally, the published Lemma 3.17 states that congruence-class support always gives \(k\) disconnected points, which contradicts our connected \(S^1\) outcome for coprime lengths. Its Conjecture 3.18 predicts \(S^{k-2}\) for congruence-class zero positions, whereas the uniform stable branch has \(S^{2k-3}\), with distinct homology degree for every \(k\ge2\). Already \((n,k)=(5,2)\) produces two circles rather than the printed predictions. The assertions may hold under further restrictions, for example when \(k\) divides \(n\); our counterexamples address the unrestricted printed statements only.

## Verification
Run the accompanying standard-library program `python3 verify.py`. It simulates parallel firing directly for each tested binary configuration, compares the complete family of maximal firing sets under the inverse-\(k\) relabeling to cyclic-interval facets, and independently calculates reduced homology by exact \(\mathbb F_2\) simplicial boundary ranks. Its recorded output is `VERIFY_OK`, with 3,252 exact orbit/nerve checks and 52 direct homology checks, including the boundary split at \((n,k)=(8,3)\). These finite checks do not replace the parameter-uniform proof, and mod-two homology alone would not determine homotopy type; the latter comes from the cited theorem.

## Relationship to prior work
Riihimäki and Smith, arXiv:2606.26786v1 (first posted 2026-06-25), define avalanche homology and establish the cyclic translation rule. Their Lemma 3.17 and Conjecture 3.18 are the motivating specifically identified gap; the printed lemma's proof treats ordinary residue classes as if they survived the \(n\)-cycle wrap-around. The authors' Theorem 3.21 discusses the consecutive-support situation, but does not identify the coprime-residue change of coordinates or these arithmetic thresholds.

Adamaszek, Adams, Frick, Peterson and Previte-Johnson, arXiv:1410.4336v1, Definition 3.2 and Theorem 3.6 (2014), already completely classify the homotopy types of circular-arc nerve complexes. The present claim is **not a new classification of these nerve complexes**. The contribution is the exact identification of the apparently disconnected residue-class avalanche dynamics with specific nerve parameters, the consequent correction to the printed avalanche statements, and the sharp residue-dependent transition. Because the earlier nerve theorem supplies the homotopy classification as a known ingredient, the work does not claim novelty for the nerve-theoretic sphere classification itself.

## Limitations
Coprimality is essential to the relabeling permutation. No homotopy formula is asserted here for \(T_a<0\), noncoprime lengths, or arbitrary multigrain configurations; additional cases can be evaluated using the corresponding cyclic-interval complexes when applicable. The proof establishes ordinary homotopy types and their reduced integral homology, not a canonical equivariant identification respecting the original cycle's geometric rotations. An unindexed prior application of the circular-arc nerve theorem to these avalanche configurations cannot be ruled out from the checked literature alone.

## References
1. H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786v1 (2026-06-25), §§2–3, especially Lemma 3.17 and Conjecture 3.18. https://arxiv.org/abs/2606.26786 .
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336v1 (2014-10-16), Definition 3.2 and Theorem 3.6. https://arxiv.org/abs/1410.4336 .
