# Square-zero skew-derivation rank spectra on star incidence algebras

## Finding
Let \(K=\mathbb F_q\) be an arbitrary finite field, let \(s,f\geq0\) with \(m=2s+f\geq1\), and let \(X\) be the height-one poset with least element \(0\) and \(m\) incomparable maximal elements. Let \(\sigma\) interchange \(s\) disjoint pairs of maximal elements and fix the other \(f\); write \(\varphi\) for its induced automorphism of the incidence algebra \(A=I(X,K)\). A \(\varphi\)-derivation is a \(K\)-linear map \(D:A\to A\) satisfying \(D(ab)=D(a)b+\varphi(a)D(b)\). We count precisely those with \(D^2=0\) (composition).

Define the rank polynomial
\[
 P_{s,f,q}(T)=\sum_{\substack{D:A\to A\\ D\text{ a }\varphi\text{-derivation},\ D^2=0}}T^{\operatorname{rank}_K D}.
\]
The complete rank distribution is
\[
\boxed{
P_{s,f,q}(T)=\begin{cases}
\left((1+(q-1)T)^2+(q^2-1)T^2\right)^s(1+(q-1)T)^f,&\operatorname{char}K\ne2,\\
\left((1+(q-1)T)^2+q(q-1)T^2\right)^s(1+(q-1)T)^f,&\operatorname{char}K=2.
\end{cases}}
\]
Consequently the numbers of square-zero \(\varphi\)-derivations are \(q^f(2q^2-1)^s\) in odd characteristic and \(q^f(q(2q-1))^s\) in characteristic two. The possible ranks are exactly the integers from \(0\) through \(m\). Since \(\dim_K A=2m+1\), for each such derivation the homology of the complex \((A,D)\) has dimension \(2m+1-2\operatorname{rank}D\). These are counts of linear operators, not counts modulo algebra automorphisms.

## Assumptions and scope
The statements concern the specified incidence algebra, the specified leaf-permutation automorphism with \(\sigma^2=1\), and finite fields of any prime-power order. There is no assumption that the characteristic is odd. The algebra has basis \(p_0=E_{00}\), \(p_i=E_{ii}\) and \(r_i=E_{0i}\) for \(1\leq i\leq m\). The only nonzero products of basis elements are \(p_i^2=p_i\) for \(0\leq i\leq m\) and \(p_0r_i=r_i=r_ip_i\). The automorphism satisfies \(\varphi(p_0)=p_0\), \(\varphi(p_i)=p_{\sigma(i)}\), \(\varphi(r_i)=r_{\sigma(i)}\). The same structural parameterization below holds over any field, although the enumerator requires a finite one.

## Proof
**Step 1: All skew derivations.** Every \(\varphi\)-derivation admits a *unique* parameterization by \(\beta_i,\delta_i\in K\) for all leaves, and \(\alpha_i\in K\) for moved leaves (with \(\alpha_i=0\) at fixed leaves), as follows:
\[
\begin{aligned}
D(p_0)&=-\sum_{i=1}^{m}\beta_i r_i,\\
D(p_i)&=\alpha_i p_i-\alpha_{\sigma(i)}p_{\sigma(i)}+\beta_i r_i,\\
D(r_i)&=\delta_i r_i-\alpha_{\sigma(i)}r_{\sigma(i)}.
\end{aligned}
\tag{1}
\]
At fixed leaves the two displayed diagonal terms cancel. To derive these formulas, apply the twisted Leibniz rule to the idempotents \(p_i\), their orthogonality \(p_ip_j=0\) for \(i\ne j\), and \(p_0+\sum_i p_i=1\) with \(D(1)=0\). Applying the rule to \(p_0r_i=r_i=r_ip_i\) then forces the formula for \(D(r_i)\). Conversely, substitutions into each of the above complete set of basis multiplication relations verify the twisted Leibniz identity; hence there are no omitted constraints. In particular, parameters associated with different \(\sigma\)-orbits are independent.

**Step 2: Fixed leaves.** For a fixed leaf \(i\), the local images are \(D(p_i)=\beta_i r_i\) and \(D(r_i)=\delta_i r_i\). The equations \(D^2(r_i)=0\) and \(D^2(p_i)=0\) require \(\delta_i^2=\beta_i\delta_i=0\); over a field this is equivalent to \(\delta_i=0\). The local image rank is \(0\) if \(\beta_i=0\), otherwise \(1\). The contribution to the rank polynomial is therefore \(1+(q-1)T\).

**Step 3: Transposed pairs.** Consider an orbit \(\{i,j\}\) with \(\sigma(i)=j\). Write \(u=\alpha_i\), \(v=\alpha_j\), \(d_i=\delta_i\), \(d_j=\delta_j\), \(b_i=\beta_i\) and \(b_j=\beta_j\). Squaring the maps in (1) and comparing coefficients gives the necessary-and-sufficient relations
\[
\begin{gathered}
 u(u+v)=v(u+v)=0,\quad d_i^2+uv=d_j^2+uv=0,\\
 u(d_i+d_j)=v(d_i+d_j)=0,\\
 b_i(u+d_i)=0,\quad b_j(v+d_j)=0,\\
 u(b_i+b_j)=v(b_i+b_j)=0.
\end{gathered}
\tag{2}
\]
The equations for \(D^2(p_0)\) follow from those for \(D^2(p_i)\) and \(D^2(p_j)\), because \(D(p_0)=-\sum_i D(p_i)\). When \(u=0\), equations (2) force \(v=d_i=d_j=0\) and leave \(b_i,b_j\) independent and arbitrary. Such an operator has local rank the number of its nonzero \(b\)-parameters, contributing \((1+(q-1)T)^2\).

When \(u\ne0\), the equations force \(v=-u\), \(d_j=-d_i\), and \(d_i^2=u^2\). If \(\operatorname{char}K\ne2\), either \(d_i=u\), which forces \(b_i=b_j=0\), or \(d_i=-u\), which permits \(b_j=-b_i\) with arbitrary \(b_i\). There are therefore \((q-1)(1+q)=q^2-1\) solutions of this type. If \(\operatorname{char}K=2\), then \(d_i=d_j=u\), and \(b_j=b_i\) with arbitrary \(b_i\), yielding \(q(q-1)\) solutions. In every \(u\ne0\) case the image has local rank \(2\): the images of a diagonal generator and a radical generator are linearly independent, while \(D^2=0\) bounds the rank on this four-dimensional local component by \(2\).

**Step 4: Additivity and the polynomial.** Images of the distinct \(\sigma\)-orbit blocks are supported on disjoint diagonal/radical basis coordinates. Moreover \(D(p_0)=-\sum_i D(p_i)\) is already in their combined image. Thus the global rank is the sum of local ranks; multiplying the independent local rank polynomials proves the boxed formula. Evaluating at \(T=1\) gives the total counts. Every rank from \(0\) to \(m\) occurs by choosing suitable \(\beta_i\) with all \(\alpha_i=\delta_i=0\). Finally, \(D^2=0\) implies \(\operatorname{im}D\subseteq\ker D\), so rank-nullity gives \(\dim\ker D/\operatorname{im}D=2m+1-2\operatorname{rank}D\).

## Verification
The accompanying standalone Python 3 program `verify_skew_star.py` implements the full incidence-algebra multiplication table, constructs the twisted-Leibniz linear equations for all matrix entries, verifies the dimension of the unrestricted twisted-derivation space and the parameterized basis maps, then exhaustively checks squares and ranks in six prime-field cases. It additionally enumerates the two-leaf transposition case over \(\mathbf F_4\) using native extension-field arithmetic. Run `python3 verify_skew_star.py`; expected terminal marker: `VERIFY_OK`. For \(s=2,f=0,q=2\), the rank distribution is \((1,4,10,12,9)\), and for \(s=1,f=0,q=3\) it is \((1,4,12)\). Computation checks only these finite instances, not the unrestricted theorem; the proof above establishes the latter.

## Relationship to prior work
Fornaroli and Khrypchenko (arXiv:2307.08439, first posted 2023-07-17), Theorem 2.8, classify skew derivations of general incidence algebras by an inner-plus-additive decomposition. Their Example 3.20 examines the two-leaf star with a leaf swap and a nontrivial cohomology class. The present question imposes the additional quadratic composition constraint \(D^2=0\) and determines its entire finite-field rank spectrum, including arbitrary numbers of swapped and fixed leaves. The abstract classification of all skew derivations does not itself state or enumerate those quadratic loci. Sánchez-Ortega (arXiv:1312.4635) treats \(\sigma\)-mappings of triangular algebras; some of its simplifying idempotent hypotheses do not hold for the split leaf-block algebra when \(m\ge2\), and it does not report this rank enumerator. Neither preceding result's generality alone warrants a claim of unique novelty; equivalent formulations may exist elsewhere.

## Limitations
Only the specified leaf-permutation automorphisms with involution cycle type are covered. No formula is asserted for arbitrary incidence-algebra automorphisms, general posets, longer leaf cycles, or conjugacy classes. Exhaustive software tests are independent finite checks rather than a proof of the infinite family. The earlier general skew-derivation classification and the cohomology calculation on the two-leaf star remain credited to their authors. A literature search cannot rule out equivalent unpublished or differently indexed prior work.

## References
1. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439v1 (2023-07-17), https://arxiv.org/abs/2307.08439. Theorem 2.8 and Example 3.20.
2. J. Sánchez-Ortega, *σ-Mappings of triangular algebras*, arXiv:1312.4635v1 (2013), https://arxiv.org/abs/1312.4635. Theorem 2.6 and accompanying hypotheses.
