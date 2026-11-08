# A Cantor survivor and a finite-capture transition in predictive tent control

## Finding

For the one-step predictive-control map \(F_{H,\vartheta}=f_H\circ(\vartheta\operatorname{id}+(1-\vartheta)f_H)\), \(f_H(x)=H\min\{x,1-x\}\), the full positive-multiplier stabilizing interval has a precise exceptional repeller and a discontinuous finite-capture law. Fix any real \(H\ge2\) and
\[
1+\frac1H<\vartheta\le\frac{H}{H-1}.
\]
Define
\[
\alpha=(H+1)\vartheta-H,\quad s=H\alpha,\quad
r=H\bigl(H-(H-1)\vartheta\bigr),\quad
R=\frac{1+H(\vartheta-1)}{\alpha},\quad J=[\tfrac12,R].
\]
Then \(0\le r<1\), \(s>2\), and \(\tfrac12<R<1\). The survivor
\[
K=\bigcap_{k\ge0}F_{H,\vartheta}^{-k}(J)
\]
is a separated two-branch self-similar Cantor repeller, conjugate to the full one-sided binary shift, with
\[
\dim_{\mathrm H}K=\frac{\log 2}{\log s},\qquad
h_{\mathrm{top}}(F_{H,\vartheta}|K)=\log2.
\]
Every real initial point outside \(K\) tends to zero; every point in \(K\) stays at least \(1/2\) from zero. Thus \(K\) is exactly the set of initial points *not attracted to zero*. In particular the basin of zero has full Lebesgue measure, even though \(F_{H,\vartheta}|K\) has repelling periodic orbits of all periods.

For \(X\) uniformly distributed on \(J\), let \(\tau=\min\{k\ge1:F_{H,\vartheta}^k(X)\notin J\}\). Then for every integer \(k\ge0\),
\[
\Pr(\tau>k)=\left(\frac{2}{s}\right)^k.
\]
The exact finite-time capture regime changes at the endpoint \(\vartheta_*=H/(H-1)\). For every strictly smaller admissible \(\vartheta\), only a countable set of initial conditions ever attains zero at a finite iterate. At \(\vartheta=\vartheta_*\), almost every real initial condition reaches zero in finite time. If \(X\) is uniform on \([0,1]\) and \(C=\min\{k\ge1:F_{H,\vartheta_*}^k(X)=0\}\), then
\[
\Pr(C>1)=\frac12,\qquad
\Pr(C>k)=\frac{(H-1)^2}{2H^2}
\left(\frac{H-1}{H^2}\right)^{k-2}\quad(k\ge2).
\]
All equalities involving probabilities are unaffected by finite boundary sets.

## Assumptions and scope

The phase space is the whole real line, not just the unit interval. The generalized tent map is \(f_H(x)=Hx\) for \(x\le1/2\) and \(f_H(x)=H(1-x)\) for \(x\ge1/2\). The feedback uses precisely *one* uncontrolled iterate: \(F_{H,\vartheta}(x)=f_H(\vartheta x+(1-\vartheta)f_H(x))\). The height \(H\ge2\) may be any real number, the gain lies in the strict/closed interval displayed above, and the first-hit time \(C\) counts iterations beginning at one. Hausdorff dimension and entropy refer to the compact repeller \(K\), not to all of \(\mathbb R\). The probability statements refer to the explicitly stated uniform initial distributions.

## Proof

**Exact three-branch formula.** Set
\[
c=\frac{\tfrac12+H(\vartheta-1)}{\alpha}.
\]
Direct substitution, including the switching values, gives
\[
F_{H,\vartheta}(x)=
\begin{cases}
rx,&x\le1/2,\\
sx+H^2(1-\vartheta),&1/2<x\le c,\\
H-sx-H^2(1-\vartheta),&x>c.
\end{cases}
\]
The gain assumptions imply \(0\le r<1\), \(s>2\), and \(1/2<c<R<\min\{1,H/2\}\). We have \(F(c)=H/2\) and \(F(R)=0\); the left and right branches map across the entire interval \(J\).

**Two exact inverse contractions.** For every \(y\in J\) the only preimages inside \(J\) are
\[
\phi_0(y)=\frac{y-H^2(1-\vartheta)}s,
\qquad
\phi_1(y)=\frac{H-H^2(1-\vartheta)-y}s.
\]
They have ratio \(1/s\), opposite orientations, and their images are disjoint, strictly interior compact subintervals of \(J\) because
\[
\frac12<\phi_0(\tfrac12)<\phi_0(R)<c<
\phi_1(R)<\phi_1(\tfrac12)<R.
\]
Consequently every sequence of binary symbols determines one nested sequence of cylinders and a unique point of \(K\). The resulting coding is a homeomorphism from the full one-sided binary shift onto \(K\), intertwining the shift with \(F\). The cylinders of depth \(k\) number \(2^k\), have equal length \(|J|s^{-k}\), and have disjoint closures. The open-set condition implies \(\dim_{\mathrm H}K=\log2/\log s\); the conjugacy proves entropy \(\log2\), as well as repelling primitive periodic orbits of every positive period.

**Basin dichotomy.** Once an orbit lands in \(( -\infty,1/2]\), it subsequently follows the scalar recursion \(x\mapsto rx\) and hence converges to zero (and becomes identically zero after the first such step when \(r=0\)). If a point exits \(J\) above \(R\), the next iterate is strictly negative, hence enters this contraction branch. A point initially greater than \(R\) similarly has negative next iterate. Every real point not in \(K\) eventually follows the contracting branch; every orbit in \(K\) remains in \([1/2,R]\), so zero is not its limit. Since \(2/s<1\), \(K\) has zero Lebesgue measure.

**Exact exit law.** Starting uniformly in \(J\), the points surviving through \(k\) iterates of the map form the \(2^k\) depth-\(k\) cylinders, each of length \(|J|s^{-k}\). Their total normalized length is exactly \((2/s)^k\), for every \(k\ge0\).

**Finite capture and the endpoint.** For an interior gain \(r>0\), every affine branch of \(F\) has nonzero slope, so \(F^{-k}(\{0\})\) is finite for each integer \(k\ge1\). Their union is countable, though the complement of \(K\) still converges to zero. At the endpoint \(r=0\), all points outside \(K\) reach zero after finitely many iterates by the basin proof. For \(X\in[0,1]\), the event \(C>1\) is precisely \(X>1/2\), except for boundary points. The event \(C>2\) is \(X\in J\) and \(F(X)>1/2\), which has Lebesgue length \((H-1)/s=(H-1)^2/(2H^2)\) because the tent apex has height \(H/2\) and both rising/falling slopes have magnitude \(s=2H^2/(H-1)\). For each additional non-capture iterate, the image must pass through \(J\) once more; the two inverse branches multiply the relevant Lebesgue length by \(2/s=(H-1)/H^2\). This proves the complete tail. Finally at the excluded lower gain \(\vartheta=1+1/H\), the scalar branch has \(r=1\) and every \(x\le1/2\) is fixed, showing why the strict lower bound matters.

## Verification

The accompanying standalone `check.py` uses rational arithmetic only. Across five rational tent heights and four gain selections per height, it tests the three-branch formula, both inverse branches, their strict separation, the first seven cylinder counts and lengths, and fixed points of both inverse branches. It independently subdivides the endpoint map into exact-rational affine pieces through eight iterations and compares the survivor lengths with the stated capture law. It completed 980 assertions. These finite checks corroborate the identities but are not a proof for all real parameters; the preceding argument supplies the parameter-uniform proof. Reproduce with `python check.py` using Python's standard library.

## Relationship to prior work

Ayers, Dmitrishin, Radunskaya, A. Stokolos and C. Stokolos (arXiv:2111.08904v1) introduced exactly this predictive-control composition and proved broad boundedness and convergence-versus-nonconvergence alternatives, including their Lemmas 1 and 2 for the positive-multiplier regime. The present contribution is the explicit two-branch exceptional set *for the controlled map*, its dimension and entropy, the exact geometric exit law, and the all-real-initial-state distinction between eventual convergence and finite-time capture. That work's classical Cantor repeller of the **uncontrolled** generalized tent map is a different invariant set and is not claimed as new.

Place and Arrowsmith (2000) derive exact first-entry statistics for a generalized tent map in the pre-control stage of an Ott–Grebogi–Yorke fixed-point-targeting procedure. Their uncontrolled pre-control dynamics and separately activated feedback differ from the predictive composition studied here. General separated-iterated-function-system theory supplies the dimension technique once the inverse branches have been derived; the novelty claim is not for that general technique. Literature-priority uncertainty remains, especially if earlier treatments of the same composition used different notation.

## Limitations

The theorem covers one-step predictive feedback only, not feedback targeted at cycles of length greater than one, nor gains outside the indicated interval. For strictly interior gains the time needed to *approach* zero is infinite for almost every initial point, whereas the finite capture law applies only to the endpoint. There is no claim of independent verification or mathematical uniqueness in all published literature. The probability law concerns specified uniform ensembles; it does not assert a universal probability law for arbitrary initial measures.

## References

1. Ayers, Dmitrishin, Radunskaya, A. Stokolos and C. Stokolos. *Search for Invariant Sets of the Generalized Tent Map*. arXiv:2111.08904v1 (first publicly posted 2021-11-17), https://arxiv.org/abs/2111.08904.
2. C. M. Place and D. K. Arrowsmith. *Control of Transient Chaos in Tent Maps near Crisis I: Fixed Point Targeting*. Manuscript dated 2000-01-07, https://maths.qmul.ac.uk/~arrow/CMPDKAP1.PDF.
