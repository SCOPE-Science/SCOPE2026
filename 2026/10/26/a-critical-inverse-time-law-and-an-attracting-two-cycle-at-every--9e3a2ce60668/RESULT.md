# A critical inverse-time law and an attracting two-cycle at every supercritical GeCo2 step

## Finding
For the symmetric two-state exchange equation, the second-order geometric conservative (GeCo2) scheme has a sharp nonlinear transition at a finite normalized step. At the critical step its equilibrium attracts **every** strictly positive, mass-conserving initialization at an exact inverse-iteration rate, despite the derivative of the iteration map being \(-1\). Beyond that step the equilibrium loses stability, while an explicit implicit equation gives a **locally attracting symmetric primitive two-cycle for every supercritical step**, with a linear onset and a nonzero stiff-step amplitude.

Write
\[
\varphi(v)=\begin{cases}(1-e^{-v})/v,&v>0,\\1,&v=0,\end{cases}\quad
z=2h,\quad u=e^{-z},\quad t=\frac{z(1+u)}2,\quad b=z(1+u)-2(1-u).
\]
There is exactly one \(z_c>0\) such that \(t(z_c)=2\); numerically \(z_c=3.9223595027430789\ldots\). Set \(b_c=b(z_c)=2(1+e^{-z_c})\).

For the strictly positive initial vector \(Y^0\), normalize the deviation by \(x_n=(Y^n_1-Y^n_2)/(Y^0_1+Y^0_2)\). For any \(z\ge z_c\), the exact GeCo2 evolution is
\[
 x_{n+1}=-x_n p_z(|x_n|),\qquad
 p_z(r)=t(z)\varphi\!\left(\frac{b(z)r}{1+r}\right)-1.
\]
Then:

1. **Critical case.** At \(z=z_c\), every \(x_0\in(-1,1)\setminus\{0\}\) gives alternating signs and \(x_n\to0\), with the sharp asymptotic
\[
 \lim_{n\to\infty} n|x_n|=\frac1{b_c}=0.4902949378428849\ldots.
\]
2. **Supercritical case.** For each \(z>z_c\) there is a unique \(r_z\in(0,1)\) solving
\[
 t(z)\varphi\!\left(\frac{b(z)r_z}{1+r_z}\right)=2.
\]
The two normalized states \(+r_z\) and \(-r_z\) form a primitive two-cycle of the original GeCo2 method. The cycle is locally asymptotically attracting. With \(v_z=b(z)r_z/(1+r_z)\), its one-step amplitude multiplier and two-step Floquet multiplier are
\[
 \mu_z=1-\bigl(2-t(z)e^{-v_z}\bigr)\bigl(1-v_z/b(z)\bigr),
 \qquad\mathcal M_z=\mu_z^2<1.
\]
3. **Two endpoint laws.** Immediately after the critical step, the period-two amplitude turns on **linearly**, not at a square-root rate:
\[
 r_z=\frac{1+(1-z_c)e^{-z_c}}{2b_c}(z-z_c)+O((z-z_c)^2)
      =0.2309666286116636\ldots\,(z-z_c)+O((z-z_c)^2).
\]
For arbitrarily stiff positive steps,
\[
 \lim_{z\to\infty} r_z=\frac13,\qquad
 \lim_{z\to\infty}\mu_z=-\frac12,
 \qquad\lim_{z\to\infty}\mathcal M_z=\frac14.
\]
All assertions concern exact arithmetic and the symmetric exchange problem.

## Assumptions and scope
The ODE is \(Y'=AY\), where \(A=\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\) and \(Y_1^0,Y_2^0>0\). Its conserved mass is \(M=Y^0_1+Y^0_2>0\), and \(|x_0|<1\). The equilibrium is \((M/2,M/2)\), and the continuous-time nonconserved mode has rate \(-2\). Time step \(h>0\), normalized by \(z=2h\).

The GeCo2 scheme is the published two-stage map (Izgin–Kopecz–Martiradonna–Meister, Equations (50)–(51)):
\[
 Y^{(2)}=Y+h\varphi(z)AY,\qquad
 W=2\varphi(z)AY-AY-AY^{(2)},
\]
\[
 Y^+=Y+\frac h2\varphi\!\left(h\sum_{i=1}^{2}\frac{\max(0,W_i)}{Y_i}\right) A(Y+Y^{(2)}).
\]
This same published recurrence and its local linear stability test are prior results, not new claims. The present assertions quantify nonlinear behavior exactly at and beyond the boundary on this one-parameter symmetric family. Neither global attraction toward the nonzero cycle for all starts nor uniqueness of arbitrary nonsymmetric periodic orbits is asserted.

## Proof
**1. Reduction from the actual two-stage rule.** Since \(A^2=-2A\), the stage becomes \(Y^{(2)}=Y+(1-u)AY/2\), and its normalized deviation is \(x^{(2)}=u x\). Directly from the displayed formula for \(W\),
\[
 W=\left(\frac{2(1-u)}z-(1+u)\right)AY
   =-\frac bz AY.
\]
Here \(b>0\) because \(b=(1+u)(z-2\tanh(z/2))\) and \(\tanh s<s\) for \(s>0\). Also \(AY=(-Mx,Mx)^{\mathsf T}\). For either sign of \(x\), exactly one component of \(W\) is positive; using \(Y_{1,2}=M(1\pm x)/2\) yields
\[
 h\sum_i \frac{\max(0,W_i)}{Y_i}=\frac{b|x|}{1+|x|}.
\]
Finally \(A(Y+Y^{(2)})=(1+u)AY\), and the normalized signed update is \(x^+=x[1-t\varphi(b|x|/(1+|x|))]=-x p_z(|x|)\). Mass conservation and strict positivity of the GeCo2 step are established for this method in the motivating publication; they also follow on the region used below from \(0<p_z(r)<t-1\) and the stated bounds.

**2. Global boundary inequalities.** The function \(t(z)\) is strictly increasing because
\[
 t'(z)=\frac{1+(1-z)e^{-z}}2>0 \quad(z>0).
\]
For \(z\le1\) this is immediate; for \(z>1\), \((z-1)e^{-z}\le e^{-2}<1\). Also \(t(3)<2<t(4)\), giving the unique \(z_c\in(3,4)\). For every \(z\ge z_c\), \(t\ge2\) and \(u<e^{-3}<1/20\). At \(r=1\), put \(v=b/2=t-(1-u)>1\). Then \(v<t<v+1\), and
\[
 t e^{-v}<(v+1)e^{-v}\le 2/e<3/4<1-u.
\]
Consequently \(t(1-e^{-v})>t-(1-u)=v\), while \(t(1-e^{-v})<t<2v\). Division by \(v>0\) proves
\[
 0<p_z(1)=t\varphi(b/2)-1<1.
\]
Because \(\varphi'(v)<0\) for \(v>0\) (equivalent to \(e^v>1+v\)), \(p_z(r)\) decreases strictly on \([0,1]\), from \(p_z(0)=t-1\). In particular, at criticality \(0<p_{z_c}(r)<1\) for every \(r\in(0,1)\), and for supercritical steps \(p_z(0)>1>p_z(1)>0\).

**3. Critical global relaxation.** At \(z=z_c\), the amplitude obeys \(r_{n+1}=r_n p_{z_c}(r_n)\). By Step 2 the positive sequence decreases, and any positive limit would violate \(p_{z_c}(r)<1\); hence \(r_n\downarrow0\). The sign alternates at every step. Taylor expansion of \(\varphi(v)=1-v/2+O(v^2)\) and \(br/(1+r)=br+O(r^2)\) gives
\[
 p_{z_c}(r)=1-b_c r+O(r^2),\qquad
 r_{n+1}=r_n-b_c r_n^2+O(r_n^3).
\]
Thus \(r_{n+1}^{-1}-r_n^{-1}=b_c+O(r_n)\to b_c\). Averaging telescoping differences proves \(r_n^{-1}/n\to b_c\), or \(nr_n\to b_c^{-1}\), for **every** strictly positive non-equilibrium start.

**4. Existence and local stability of the two-cycle for every supercritical step.** Strict monotonicity and the endpoint comparison in Step 2 give exactly one \(r_z\in(0,1)\) with \(p_z(r_z)=1\). Oddness of \(x\mapsto-xp_z(|x|)\) shows \(r_z\mapsto-r_z\mapsto r_z\). Because \(r_z>0\), this is primitive period two.

On positive amplitudes the map is \(g(r)=r p_z(r)\). Write \(v=br/(1+r)\). Using
\[
 -v\varphi'(v)=\varphi(v)-e^{-v},\quad
 r\frac{dv}{dr}=v\left(1-\frac vb\right),\quad
 t\varphi(v_z)=2,
\]
we obtain
\[
 g'(r_z)=1-\bigl(2-t e^{-v_z}\bigr)\bigl(1-v_z/b\bigr)=\mu_z.
\]
The strict inequality \(e^{-v}<\varphi(v)\) for \(v>0\) gives \(0<2-t e^{-v_z}<2\); also \(0<v_z<b\). Therefore \(0<(2-t e^{-v_z})(1-v_z/b)<2\), so \(-1<\mu_z<1\). The derivative of the signed step at both cycle points is \(-\mu_z\), giving return multiplier \(\mu_z^2<1\). The cycle is hence locally asymptotically attracting.

**5. Linear onset and stiff limit.** For \(r\ge0\), let \(F(z,r)=t(z)\varphi(br/(1+r))-2\). At \((z_c,0)\), \(F=0\), \(\partial_rF=-b_c\ne0\), and \(\partial_zF=t'(z_c)\). The one-sided implicit function theorem yields \(r_z=t'(z_c)(z-z_c)/b_c+O((z-z_c)^2)\). The signed map contains a \(x|x|\) nonlinearity at equilibrium, explaining the nonsquare-root onset.

As \(z\to\infty\), \(t/z\to1/2\), \(b/z\to1\). For every fixed \(r\in(0,1)\), \(br/(1+r)\to\infty\), so
\[
 t\varphi\left(\frac{br}{1+r}\right)\longrightarrow\frac{1+r}{2r}.
\]
The limit equals \(2\) only at \(r=1/3\); by monotonicity, for fixed \(r<1/3\) the left side eventually exceeds \(2\) and for \(r>1/3\) it eventually falls below \(2\). Thus \(r_z\to1/3\). At the root, \(v_z\to\infty\), \(v_z/b=r_z/(1+r_z)\to1/4\), and \(t e^{-v_z}\to0\). The multiplier formula gives \(\mu_z\to1-2(3/4)=-1/2\), hence \(\mu_z^2\to1/4\).

## Verification
The companion `verify.py` implements the original **componentwise two-stage map** independently from the derived scalar map. It checks the stage reduction, positive states and conserved mass, the critical root and reciprocal coefficient, the supercritical root and period-two relation over several step sizes, the finite-difference multiplier, and the limiting asymptotic sample behavior. The routine is deterministic and uses only Python's standard library. Those finite checks support arithmetic reproducibility; all universal and infinite-time conclusions are proved in the preceding section, not inferred from the tests. The closed-form critical and multiplier identities have also been re-derived symbolically.

## Relationship to prior work
Izgin, Kopecz, Martiradonna and Meister (2023), Section 4.1, Equations (50)–(51), Lemma 4.2 and Theorem 4.3, introduce the exact specialized two-stage map, establish its differentiability, and characterize hyperbolic local stability through \(R(-z)=1-z(1+e^{-z})/2\). Their Section 5.1 also documents observed persistent post-boundary oscillations. Those ingredients are prior work. The present claim instead resolves **the previously unaddressed equality case globally** and supplies a genuine analytic attracting two-cycle for **every** larger step, its precise Floquet multiplier, its linear small-amplitude onset, and its large-step limit. A related method with a different recurrence would not imply these statements without reducing to the same GeCo2 map.

Searches for GeCo2 cycles, critical relaxation, aliases and broader numerical-bifurcation results did not find an exact covering theorem in the inspected available source. Such non-detection is not proof of priority; a specialist equivalence in other literature remains a risk. The GeCo method's original 2020 article was identifiable, but its full publisher/repository text was not accessible in this pass; its existence and the formulas it established are acknowledged rather than treated as fully inspected.

## Limitations
The results require equal bidirectional exchange rates, two components, strictly positive states and exact GeCo2, not arbitrary reaction networks, the asymmetric rates of the originating numerical test, or other geometric integrators. The claim proves **local**, not global, attraction to the postcritical two-cycle; it does not classify all possible nonsymmetric periodic orbits or floating-point behavior. The mathematical review here is not an independent audit. Publication-priority uncertainty persists despite actual source and record searches.

## References
1. T. Izgin, S. Kopecz, A. Martiradonna and A. Meister, *On the Dynamics of First and Second Order GeCo and gBBKS Schemes*, arXiv:2301.10658v1, publicly posted 2023-01-25. https://arxiv.org/abs/2301.10658. Specific material: Section 4.1, Equations (50)–(51), Lemma 4.2, Theorem 4.3, and Section 5.1.
2. A. Martiradonna, F. Colonna and F. Diele, *GeCo: Geometric Conservative nonstandard schemes for biochemical systems*, Applied Numerical Mathematics (2020), DOI:10.1016/j.apnum.2019.12.004. Historical method source; complete publisher/repository text not inspected.
