# Minimal-order classification of scalar quadratic null forms for cubic \(O(2)\)-Hopf coefficients
## Finding
Let \(K=\partial_xP(-\partial_x^2)\) be a real constant-coefficient odd multiplier. Let \(N\) be a real constant-coefficient symmetric bilinear differential operator on scalar \(2\pi\)-periodic functions, defined on Fourier modes by
\[
N(e^{ikx},e^{i\ell x})=b(k,\ell)e^{i(k+\ell)x},
\]
with \(b(k,\ell)\in\mathbb R[k,\ell]\), \(b(k,\ell)=b(\ell,k)\), and \(b(-k,-\ell)=b(k,\ell)\). Put
\[
F_2(u,v)=\bigl(0,N(u,u)\bigr)^\top,\qquad F_3=0.
\]
Assume that, for every integer \(m\ge 1\),
\[
b(m,m)=0,\qquad b(-m,2m)=0.
\]
Then, whenever the relevant \(O(2)\)-Hopf pair is admissible, adding \(KF_2\) to an arbitrary other reflection-compatible conservative quadratic/cubic flux with the same multiplier changes none of the four cubic extraction coefficients and therefore changes neither normal-form coefficient \(\zeta\) nor \(\xi\).

The two interaction cancellations hold for every \(m\ge1\) if and only if
\[
b(k,\ell)=(k-\ell)^2(2k+\ell)(k+2\ell)\,h(k,\ell),
\]
where \(h\in\mathbb R[k,\ell]\) is symmetric and even under simultaneous sign reversal. Hence every nonzero member of this scalar quadratic interactionwise-null class has differential order at least \(4\). At order exactly \(4\), \(h\) is constant, so the symbol is unique up to scale:
\[
b(k,\ell)=c\,(k-\ell)^2(2k+\ell)(k+2\ell),\qquad c\in\mathbb R\setminus\{0\}.
\]
This is exactly the symbol of the order-\(4\) null form in arXiv:2609.22779v1.

## Assumptions and scope
The claim is restricted to constant-coefficient scalar quadratic perturbations of the form \(F_2=(0,N(u,u))^\top\). “Interactionwise cubic-null” means that the perturbation vanishes on the two Fourier interactions that can feed the cubic \(O(2)\)-Hopf coefficients at a critical mode \(m\): the critical-critical interaction \((m,m)\), and the critical/second-harmonic interaction \((-m,2m)\). The zero-output interaction \((m,-m)\) is annihilated by the odd multiplier \(K\).

The claim does not classify arbitrary two-component quadratic fluxes, cubic fluxes, derivative-dependent cancellations that arise by a different mechanism, or cancellations that hold only for one chosen critical wavenumber or one chosen linear part. Those broader cases remain outside the theorem.

For a constant-coefficient bilinear differential operator written in polarized form, the highest derivative falling on the first input is \(\deg_k b\), and the highest derivative falling on the second input is \(\deg_\ell b\). Thus its differential order is \(\max\{\deg_k b,\deg_\ell b\}\). Because the universal factor below has degree \(4\) in each variable, every nonzero symbol in the classified class has differential order at least \(4\). For nonzero \(K\), composition by the output multiplier raises this order by \(\operatorname{ord}K\).

## Proof
Because \(m\mapsto b(m,m)\) is a one-variable polynomial that vanishes at every positive integer, it vanishes identically. Therefore \(b(k,\ell)\) vanishes on the line \(k=\ell\), so \(k-\ell\) divides \(b\). Write
\[
b(k,\ell)=(k-\ell)c(k,\ell).
\]
Symmetry of \(b\) gives
\[
(k-\ell)c(k,\ell)=b(k,\ell)=b(\ell,k)=-(k-\ell)c(\ell,k),
\]
hence \(c(\ell,k)=-c(k,\ell)\). Thus \(c(k,k)=0\), so \(k-\ell\) divides \(c\) as well. Consequently
\[
(k-\ell)^2\mid b(k,\ell).
\]

Likewise, \(m\mapsto b(-m,2m)\) is a polynomial vanishing at every positive integer, hence it is identically zero. Thus \(b\) vanishes on the line \(2k+\ell=0\), so
\[
2k+\ell\mid b(k,\ell).
\]
By symmetry, \(b(2m,-m)=b(-m,2m)=0\) for all \(m\), so \(b\) also vanishes on \(k+2\ell=0\), giving
\[
k+2\ell\mid b(k,\ell).
\]
The three linear factors \(k-\ell\), \(2k+\ell\), and \(k+2\ell\) are pairwise nonassociate and therefore relatively prime in \(\mathbb R[k,\ell]\). Combining the divisibilities yields
\[
(k-\ell)^2(2k+\ell)(k+2\ell)\mid b(k,\ell).
\]
Writing the quotient as \(h\), symmetry and simultaneous-sign evenness of \(b\), together with the same two symmetries of the degree-\(4\) factor, imply
\[
h(k,\ell)=h(\ell,k),\qquad h(-k,-\ell)=h(k,\ell).
\]
The converse is immediate because the displayed factor vanishes on \(k=\ell\), \(2k+\ell=0\), and \(k+2\ell=0\).

It remains to connect these algebraic cancellations to the cubic normal form. The cubic extraction formulas for the two-component conservative \(O(2)\)-Hopf problem involve, at quadratic order, only the critical mode and the second harmonic. The source's null-form argument shows that a quadratic perturbation of the present form contributes no critical-critical forcing when \(b(m,m)=0\). Therefore it does not change the quadratic center-manifold correction. In the outer quadratic interaction with an arbitrary existing second-harmonic correction, the only interaction that can project back to the critical mode has wavenumbers \((-m,2m)\) or one of its symmetry mates; these vanish by \(b(-m,2m)=0\), symmetry, and simultaneous-sign evenness. Interactions with total wavenumber \(3m\) are removed by the critical projection, while total wavenumber \(0\) is annihilated by \(K\). Since the perturbation has no cubic part, it adds no direct cubic term. Thus all four cubic extraction coefficients are unchanged.

As a polynomial in \(k\) over the coefficient ring \(\mathbb R[\ell]\), the universal factor has degree \(4\); the same is true with \(k\) and \(\ell\) interchanged. Hence any nonzero quotient \(h\) gives \(\deg_k b=4+\deg_k h\) and \(\deg_\ell b=4+\deg_\ell h\). Every nonzero interactionwise-null operator therefore has differential order at least \(4\). Differential order exactly \(4\) forces \(\deg_k h=\deg_\ell h=0\), so \(h\) is a nonzero constant. Finally,
\[
2(k+\ell)^4-7k\ell(k+\ell)^2-4k^2\ell^2
=(k-\ell)^2(2k+\ell)(k+2\ell),
\]
which is the Fourier symbol of
\[
N(f,g)=2\partial_x^4(fg)-7\partial_x^2(f_xg_x)-4f_{xx}g_{xx}.
\]
This identifies the unique order-\(4\) class with the example in arXiv:2609.22779v1.

## Verification
The proof is symbolic and finite: it uses polynomial identity on infinitely many integer points only to infer vanishing of one-variable restrictions, followed by exact divisibility in \(\mathbb R[k,\ell]\). No finite experiment is used to infer an infinite statement.

The normal-form step was checked against the full extraction mechanism in arXiv:2608.24376v1, where the quadratic contribution to cubic order passes only through the critical mode and second harmonic, and against the full null-form proof in arXiv:2609.22779v1. The latter proof uses exactly the cancellations \(b(\pm m,\pm m)=0\) and \(b(\mp m,\pm2m)=0\), plus annihilation of zero output by \(K\). The present argument isolates those conditions and classifies all polynomial symbols satisfying them simultaneously for every critical integer \(m\).

## Relationship to prior work
Özer, Şengül, and Tiryakioglu derive the general cubic coefficient formulas for conservative two-component \(O(2)\)-Hopf bifurcations and show that the quadratic contribution enters through the second harmonic. Şengül later exhibits the specific derivative-dependent null form
\[
N(f,g)=2\partial_x^4(fg)-7\partial_x^2(f_xg_x)-4f_{xx}g_{xx},
\]
with symbol
\[
(k-\ell)^2(2k+\ell)(k+2\ell),
\]
and proves that adding it changes none of the cubic coefficients. That paper explicitly asks whether a lower-order non-variational flux with the same property exists and poses the broader problem of identifying all invisible conservative reflection-compatible quadratic and cubic fluxes.

The present result does not solve that full problem. It solves the natural scalar quadratic interactionwise-null subproblem exactly: the source symbol is forced by the resonance geometry, is minimal in order, and is unique up to scale at the minimal order.

## Limitations
The theorem assumes one-component scalar quadratic structure inside the second flux component, constant coefficients, polynomial differential symbols, symmetry in the two bilinear inputs, and invisibility enforced interaction by interaction for every critical integer \(m\). More general invisible perturbations may exploit vector cancellations, cubic terms, cancellations between different monomials, special multiplier zeros, or dependence on a fixed linear part. None of those are ruled out here.

Searches did not identify a published statement of this exact factorization/minimality result, but absence from the checked literature is not a proof of global novelty. An unindexed folklore observation remains possible.

## References
1. S. S. Özer, T. Şengül, and B. Tiryakioglu, “Wave Selection at an \(O(2)\)-Hopf Bifurcation in Conservative Two-Component PDE Systems,” arXiv:2608.24376v1, 2026.
2. T. Şengül, “Variational Nonlinearities and Wave Selection at an \(O(2)\)-Hopf Bifurcation,” arXiv:2609.22779v1, 2026.
