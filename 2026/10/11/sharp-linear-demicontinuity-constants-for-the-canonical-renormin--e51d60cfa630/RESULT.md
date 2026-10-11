# Sharp linear demicontinuity constants for the canonical renormings of \(c\)
## Finding
For every real \(r\ge 1\), let \(c\) be the real Banach lattice of convergent sequences and define
\[
\|x\|_r=\max\{\|x\|_\infty,r|\lim_n x_n|\}.
\]
The exact demicontinuity constant of \((c,\|\cdot\|_r)\) is \(r\). Its order-continuous dual is \(\ell_1\) with its usual norm and is exactly \(r\)-norming. Under the coordinate realization of the universal completion, the Lorentz completion is \(\ell_\infty\) with Lorentz norm \(\|\cdot\|_\infty\). Finally, every norm-one Hahn--Banach extension \(L:\ell_\infty\to\mathbb R\) of the ordinary limit is positive, and
\[
\|x\|_{r,L}=\max\{\|x\|_\infty,r|Lx|\}
\]
is a lattice-norm extension to \(\ell_\infty\) with exact demicontinuity constant \(r\).

Thus, on this canonical family, the quadratic \(r^2\) constants appearing in the general order-continuous-dual norming and Lorentz/completion extension bounds can simultaneously be replaced by the sharp linear constant \(r\).

## Assumptions and scope
All spaces are real. Demicontinuity is used in the quantitative sense of the source: the least \(C\ge1\) such that whenever an upward directed family \(P\subset B_+\) has supremum \(f\) in the lattice, one has \(\|f\|\le C\). The case \(r=1\) is included. The statement concerns the particular renorming family above and does not assert that the source's quadratic constants admit a universal linear improvement for arbitrary normed lattices.

For the Lorentz-completion assertion, the universal completion of \(c\) is identified with the vector lattice \(\mathbb R^{\mathbb N}\) under coordinatewise order. The Lorentz norm is the gauge obtained from upward approximations by positive elements of the original lattice, as in the source.

## Proof
For the demicontinuity upper bound, let \(P\subset B_{(c,\|\cdot\|_r),+}\) and suppose \(P\uparrow f\) in \(c\). Every \(p\in P\) satisfies \(\|p\|_\infty\le1\), hence \(0\le f\le\mathbf 1\) coordinatewise. Therefore \(\|f\|_\infty\le1\) and \(|\lim_n f_n|\le1\), so \(\|f\|_r\le r\). For sharpness, put \(u^{(k)}=e_1+\cdots+e_k\). Then \(\|u^{(k)}\|_r=1\), while \(u^{(k)}\uparrow\mathbf1\) and \(\|\mathbf1\|_r=r\). Thus the exact constant is \(r\).

Every \(\varphi\in c^*\) has a unique representation
\[
\varphi(x)=\sum_{n\ge1}a_nx_n+\alpha\lim_nx_n,
\qquad a\in\ell_1,
\]
because the restriction to \(c_0\) is an \(\ell_1\)-functional and \(c/c_0\) is one-dimensional. Put \(v^{(k)}=\mathbf1-u^{(k)}\). Then \(v^{(k)}\downarrow0\), the \(\ell_1\)-part tends to zero on \(v^{(k)}\), and \(\lim_n v^{(k)}_n=1\); hence order continuity forces \(\alpha=0\). Conversely every \(\ell_1\)-functional is order continuous by splitting its series into a finite head and a small tail. Thus \((c,\|\cdot\|_r)^*_{oc}=\ell_1\). Its induced dual norm is exactly \(\|a\|_1\): the upper bound follows from \(\|x\|_\infty\le\|x\|_r\), and finite-support sign vectors in \(c_0\) attain arbitrary partial sums of \(\sum|a_n|\). Therefore
\[
\sup_{a\in B_{\ell_1}}\left|\sum a_nx_n\right|=\|x\|_\infty.
\]
The least constant \(K\) for which \(\|x\|_r\le K\|x\|_\infty\) for all \(x\in c\) is \(r\), with equality at \(\mathbf1\). Hence the order-continuous dual is exactly \(r\)-norming.

The coordinate lattice \(\mathbb R^{\mathbb N}\) is universally complete and contains \(c\) order densely, so it realizes the universal completion. Let \(x\ge0\) be bounded and define the finite truncations \(x^{(k)}=(x_1,\ldots,x_k,0,0,\ldots)\). Then \(x^{(k)}\in c_0\), \(x^{(k)}\uparrow x\), and \(\|x^{(k)}\|_r=\|x^{(k)}\|_\infty\le\|x\|_\infty\). This gives Lorentz norm at most \(\|x\|_\infty\). Conversely, any positive upward approximation bounded by \(s\) in \(\|\cdot\|_r\) is coordinatewise bounded by \(s\), so its supremum has sup norm at most \(s\). Thus the Lorentz norm equals \(\|x\|_\infty\), and finite Lorentz norm is equivalent to boundedness. Therefore the Lorentz completion is exactly \(\ell_\infty\).

Let \(\lambda:c\to\mathbb R\) be ordinary limit. Since \(\|\lambda\|=1\), Hahn--Banach gives a norm-one extension \(L:\ell_\infty\to\mathbb R\) with \(L(\mathbf1)=1\). Such an extension is automatically positive: if \(0\le x\le\mathbf1\), then \(\|\mathbf1-x\|_\infty\le1\), hence \(L(\mathbf1-x)\le1\), and therefore \(Lx\ge0\); scaling gives positivity for every positive \(x\). Positivity yields \(|Lx|\le L|x|\), so \(\|\cdot\|_{r,L}\) is a lattice norm and extends \(\|\cdot\|_r\). If a positive directed family in its unit ball has supremum \(f\in\ell_\infty\), then \(0\le f\le\mathbf1\), hence \(\|f\|_\infty\le1\) and \(0\le Lf\le1\), so \(\|f\|_{r,L}\le r\). The same truncations \(u^{(k)}\uparrow\mathbf1\) satisfy \(L(u^{(k)})=0\), \(\|u^{(k)}\|_{r,L}=1\), and \(\|\mathbf1\|_{r,L}=r\), proving sharpness.

## Verification
The proof is symbolic and uses no finite enumeration or numerical approximation. The critical identities were checked directly: the source's increasing truncations have unit norm and supremum of norm \(r\); the order-continuous dual annihilates the quotient functional \(\lim\); the Lorentz gauge on bounded positive sequences is squeezed between the same sup norm from both sides; and every norm-one extension of the limit is positive because it sends \(\mathbf1\) to \(1\).

The boundary case \(r=1\) reduces to the ordinary sup norm throughout. No assertion is made for \(0<r<1\), where the displayed maximum is simply the sup norm and the parameter no longer measures the same phenomenon.

## Relationship to prior work
Bilokopytov's 2026 paper introduces the quantitative notion of \(r\)-demicontinuity, records the canonical family \(\|x\|=\max\{\sup_k|x_k|,n|\lim_kx_k|\}\) on \(c\), proves an \(r^2\)-norming theorem for the order-continuous dual, and proves \(r^2\)-demicontinuous extension/completion bounds through the Lorentz construction. It then asks whether those constants can be improved. The present result answers that calibration question sharply on the paper's canonical example family: all three quadratic upper bounds collapse to the exact linear constant \(r\), and the Lorentz completion and one sharp extension norm are explicit.

Targeted searches for formulations using weak Fatou constants, convergent-sequence renormings, Lorentz completions, Banach-limit extensions, and exact order-continuous-dual norming constants did not reveal a statement implying the combined theorem above. The closest indexed related finding concerns finite-stage order-adherence bounds in general demicontinuous lattices; it does not compute the constants, dual, Lorentz completion, or extension norm of this family.

## Limitations
This is a sharp model-family result, not a universal improvement of the general \(r^2\) theorems. It exhibits a large class of sharp extension norms on \(\ell_\infty\) but does not classify all lattice-norm extensions of \(\|\cdot\|_r\). An older equivalent calculation may exist in the weak-Fatou literature under different notation; this remains the principal originality risk.

## References
1. E. Bilokopytov, *Variants of order semicontinuity in Banach lattices*, arXiv:2609.03070v1 (2026). Relevant items: Example 3.2, Proposition 3.10, Theorem 6.1, and Question 6.2.
