# Sharp sparse self-regulation threshold for obligate mutualistic communities

## Finding

Consider \(n\ge2\) obligate mutualists with equal intrinsic loss \(a>0\), equal pairwise mutualistic benefit \(b>0\), pairwise self-limitation \(d>0\), and optional species-specific third-order self-limitation:
\[
\dot z_i=z_i\left(-a-dz_i+b\sum_{j\ne i}z_j-h_i z_i^2\right),\qquad z_i\ge0,\quad h_i\ge0.
\]
Assume the pairwise mutualism is strong, \(B:=(n-1)b-d>0\). Call species \(i\) regulated when \(h_i>0\); let \(m\) be the number regulated and \(k=n-m\) the number unregulated.

**Theorem (minimal intervention and exact symmetric fold).** There is some choice of the \(h_i\), with exactly \(m\) positive, for which the system has a strictly positive equilibrium with strictly Hurwitz Jacobian **if and only if**
\[
 k\le\left\lceil\frac d b\right\rceil,
 \quad\text{equivalently}\quad
 m\ge n-\left\lceil\frac d b\right\rceil.
\]
In particular, the right-hand side is a positive integer and is the exact minimum number of species needing third-order self-limitation. For each admissible \(m\), choose the same \(h>0\) on the regulated species and zero elsewhere. Put
\[
 D=d-b(k-1)>0,\quad C=\frac{B(d+b)}D,\quad E=\frac{a(d+b)}D,
 \qquad h_{\rm fold}=\frac{B^2(d+b)}{4aD}.
\]
The convention \(D=d+b\) for \(k=0\) makes the same formulas valid when every species is regulated. For every \(0<h<h_{\rm fold}\) there are two equilibria with common regulated abundance \(x_-<x_+\) and (when \(k>0\)) common unregulated abundance \(y_-<y_+\):
\[
 x_{\pm}=\frac{C\pm\sqrt{C^2-4hE}}{2h},\qquad
 y_{\pm}=\frac{bm x_{\pm}-a}{D}.
\]
The upper equilibrium is strictly linearly asymptotically stable; the lower is linearly unstable with exactly one positive eigenvalue. At \(h=h_{\rm fold}\), these two equilibria coalesce in a nondegenerate fold with one zero eigenvalue; beyond that value there is no equilibrium *in this two-class-equal family*. This last statement is not a classification of all potentially asymmetric positive equilibria.

A rational witness illustrates the sharpness: with \(n=4\), \(a=b=1\), \(d=3/2\), precisely two regulated species are necessary and sufficient. With \(h_1=h_2=5/2\), \(h_3=h_4=0\), the upper equilibrium is \((2,2,6,6)\), strictly stable, and the lower equilibrium is \((1,1,2,2)\), unstable. Regulating only one of the four cannot stabilize any positive equilibrium, regardless of its regulation strength.

## Assumptions and scope

All dynamics are deterministic continuous-time polynomial Lotka–Volterra extensions on the nonnegative orthant. The only freely introduced interactions are negative cubic self-terms \(-h_i z_i^3\) in the population equations; cross-species higher-order coefficients are forbidden. The baseline coefficients \(a,b,d\) remain unchanged. All stability claims concern local linear (Hurwitz) stability of a strictly positive fixed point in full \(n\)-dimensional state space, not global attraction. Repeated indices in the usual higher-order interaction tensor are necessary for a self-cubic term.

For completeness, if \(B\le0\), the model has no strictly positive equilibrium for any \(h_i\ge0\): summing the per-capita equilibrium equations gives \(0=-na+B\sum_i z_i-\sum_i h_i z_i^2<0\). Thus the stated strong-mutualism hypothesis isolates the regime where regulation can rescue coexistence. No finite population or stochastic interpretation is assumed.

## Proof

**1. Universal lower bound on the number of regulated species.** At any positive equilibrium \(z^*\), the Jacobian factors as \(J=\operatorname{diag}(z^*)K\), where \(K\) is the symmetric matrix with off-diagonal entries \(b\) and diagonal entries \(-d-2h_i z_i^*\). Consequently \(J\) is similar to the symmetric matrix \(\operatorname{diag}(\sqrt{z^*})K\operatorname{diag}(\sqrt{z^*})\). Thus \(J\) is Hurwitz exactly when \(K\) is negative definite.

Restrict \(K\) to the \(k\) unregulated species. Its principal block is
\[
 K_{UU}=-(d+b)I_k+b\mathbf1_k\mathbf1_k^{\mathsf T},
\]
whose eigenvalues are \(-d+b(k-1)=-D\) and \(-(d+b)\) (multiplicity \(k-1\)). If \(k\ge1\) and \(D\le0\), this principal block is not negative definite, so neither is \(K\). In fact \(K\) has a strictly positive eigenvalue: for \(D<0\) this follows by the Rayleigh principle; for \(D=0\) and \(m>0\), use a vector with positive entries on the unregulated block and a sufficiently small common positive entry on regulated coordinates, whose quadratic form is positive because the cross-block coefficient \(b\) is positive. The case \(m=0\) already has \(D=-B<0\). Thus no positive equilibrium is locally asymptotically stable whenever \(D\le0\). The condition \(D>0\) is equivalent for integer \(k\) to \(k\le\lceil d/b\rceil\).

**2. Positive equilibria with exactly \(m\) regulated species.** Assume \(D>0\), hence \(m>0\). Choose a common coefficient \(h>0\) on those \(m\) species. On the invariant subspace where all regulated species equal \(x\) and all unregulated species equal \(y\), the unregulated balance (when \(k>0\)) reads \(D y=bm x-a\), so \(y=(bm x-a)/D\). Substitution into the regulated balance gives
\[
 h x^2-Cx+E=0,
 \qquad C=\frac{B(d+b)}D,
 \quad E=\frac{a(d+b)}D.
\]
For \(k=0\), the same quadratic follows directly with \(D=d+b\), \(C=B\), and \(E=a\). The discriminant vanishes at \(h_{\rm fold}=C^2/(4E)\). When \(0<h<h_{\rm fold}\), its two roots are distinct and positive. Both exceed \(E/C=a/B\), as can be seen from \(x_-=2E/(C+\sqrt{C^2-4hE})>E/C\). If \(k>0\), the inequality \(bm-B=D>0\) gives \(bm x_\pm>a\), hence \(y_\pm>0\).

**3. Full-state stability and exact fold.** For \(k>0\), the symmetric matrix \(K\) has eigenvalue \(-(d+b)-2hx\) on the \((m-1)\)-dimensional regulated transverse space and \(-(d+b)\) on the \((k-1)\)-dimensional unregulated transverse space. On normalized group-constant coordinates its remaining \(2\times2\) block is
\[
 \begin{pmatrix}
 b(m-1)-d-2hx & b\sqrt{mk}\\
 b\sqrt{mk} & -D
 \end{pmatrix},
\]
with determinant \(D(2hx-C)\). Since \(D>0\), this block is negative definite precisely when \(2hx>C\). The identity \(hx=C-E/x\), valid at every displayed equilibrium, implies that this is equivalent to \(x>2E/C=2a/B\). The roots straddle \(2E/C\): \(x_-<2E/C<x_+\). Therefore the upper equilibrium is strictly stable, whereas the lower has exactly one positive Jacobian eigenvalue and the others negative. For \(k=0\), the collective eigenvalue of \(K\) is \(B-2hx\) and the \(n-1\) transverse eigenvalues are \(-(d+b)-2hx\), giving the identical conclusion.

At the double root \(x=2E/C\), the collective eigenvalue is zero, while every transverse eigenvalue remains negative. The scalar equation \(h x^2-Cx+E=0\) has nonzero second derivative \(2h\) and nonzero derivative \(x^2\) with respect to \(h\), yielding a nondegenerate saddle-node in the two-class-symmetric invariant subspace. This completes both directions of the minimum-regulation criterion and the explicit branch classification. \(\square\)

## Verification

The standalone `check_sparse_mutualism.py` uses exact rational arithmetic, checks equilibrium balances for both branches, and tests symmetric Jacobian negative definiteness by Sylvester's criterion on 964 parameter-and-group configurations with \(2\le n\le8\). It also verifies the fold coefficient and the necessity inequality in these samples. Execute `python check_sparse_mutualism.py` from the directory containing this document; expected output begins `PASS: 964 exact parameter/group configurations`. A direct rational witness is \(a=b=1\), \(d=3/2\), \(n=4\), \(m=2\), \(k=2\), \(D=1/2\), \(h_{\rm fold}=45/16\), and \(h=5/2\), giving the two fixed points stated above. Finite computations are not the infinite proof; the proof is the matrix and quadratic argument above.

## Relationship to prior work

Çelik, Isoldi, Portakal, and Zucal (2026), Theorems 3.1 and 4.2, establish impossibility of stable coexistence for obligate mutualism under pairwise interactions and a general rescue theorem allowing freely signed quadratic and cubic higher-order terms in per-capita dynamics. The present result does not claim either of those general facts: it imposes the biologically restrictive and sparse intervention \(-h_i z_i^2\) in per-capita growth, proves the *minimal number* of species requiring it, and gives a sharp parameterized fold and full-dimensional stability test. The general unconstrained rescue theorem does not imply this constrained minimum or its threshold.

Hale and Valdovinos (2021) review two-species saturation and Allee-type coexistence thresholds, and Vet, Gelens, and Gonze (2020) study mutualistic cross-feeding bistability. These establish the broader ecological relevance and known occurrence of paired stable/unstable coexistence states; the new claim is restricted to the explicit multispecies complete-mutualism model and its exact sparse stabilization count, not the existence of saddle-nodes in mutualism per se. The negative-definite principal-block criterion is a classical linear algebra ingredient, not claimed as new.

## Limitations

The result assumes identical intrinsic loss, identical pairwise couplings, a complete reciprocal interaction network, and no higher-order cross-species terms; it does not apply unchanged to heterogeneous or directed mutualistic networks. Regulation coefficients can be very small on the stable upper branch, but then the stable abundances become arbitrarily large; there is no claim of ecologically bounded or globally attracting biomass. Above the stated fold threshold, only the two-class-equal equilibrium family is ruled out, not every asymmetric branch. Absolute historical priority is not proven: an equivalent sharp sparse-control result under different terminology may exist. No independent external audit was conducted.

## References

1. T. Ö. Çelik, V. A. Isoldi, I. Portakal, and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1, first submitted 2026-09-08, especially Theorems 3.1 and 4.2. https://arxiv.org/html/2609.09286
2. K. R. S. Hale and F. S. Valdovinos, *Ecological theory of mutualism: Robust patterns of stability and thresholds in two-species population models*, Ecology and Evolution (2021), doi:10.1002/ece3.8453. https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.8453
3. S. Vet, L. Gelens, and D. Gonze, *Mutualistic cross-feeding in microbial systems generates bistability via an Allee effect*, Scientific Reports 10, 7763 (2020), doi:10.1038/s41598-020-63772-4. https://www.nature.com/articles/s41598-020-63772-4
