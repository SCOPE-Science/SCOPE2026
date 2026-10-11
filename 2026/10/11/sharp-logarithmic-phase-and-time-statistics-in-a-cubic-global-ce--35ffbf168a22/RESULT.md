# Sharp logarithmic phase and time statistics in a cubic global center

## Finding
For every \(\kappa>0\) consider the cubic differential system in **original physical time**
\[
\dot x=y(1+\kappa x^2),\qquad \dot y=-x(1+\kappa y^2).
\]
For every amplitude \(A>0\), denote by \(T(A)\) the minimal period of the orbit starting at \((x(0),y(0))=(A,0)\). Set
\[
Q=1+\kappa A^2,\qquad L=\log Q,\qquad
U_A(s)=\frac{\log(1+\kappa x(sT(A))^2)}{L},\quad 0\le s\le1.
\]
Define the continuous triangular function
\[
U_\infty(s)=\begin{cases}|1-4s|,&0\le s\le1/2,\\ |3-4s|,&1/2\le s\le1.\end{cases}
\]
Then the following joint sharp statements hold as \(A\to\infty\) with \(\kappa\) fixed:
\[
\|U_A-U_\infty\|_\infty\longrightarrow0,
\qquad L\|U_A-U_\infty\|_\infty\longrightarrow 2\log 2.
\]
Let \(\nu_A=(U_A)_\#(ds)\) be the probability distribution on \([0,1]\) obtained by sampling a full orbit at uniform *physical-time phase* \(s\). Then
\[
\nu_A\xrightarrow{\mathrm{TV}}\mathrm{Leb}_{[0,1]},\qquad
L\,d_{\mathrm{TV}}(\nu_A,\mathrm{Leb}_{[0,1]})\longrightarrow4\log2.
\]
Here \(d_{\mathrm{TV}}(\mu,\eta)=\sup_{B}|\mu(B)-\eta(B)|=\tfrac12\int|d\mu-d\eta|\) for probability measures with densities. The period additionally obeys
\[
T(A)=\frac{2}{\sqrt Q}\big(L+4\log2+o(1)\big).
\]
The complementary energy-logarithm coordinate satisfies the **exact identity**
\[
\frac{\log(1+\kappa y(sT(A))^2)}{L}=1-U_A(s).
\]
The principal contribution is the *sharp global phase* and *total-variation time-statistics* law; the period formula is supplied to normalize the physical time and is consistent with classical complete-elliptic-integral asymptotics.

## Assumptions and scope
All parameters \(\kappa>0\) and amplitudes \(A>0\) are allowed. The limits are for \(A\to\infty\) at fixed \(\kappa\); no uniformity as \(\kappa\to0\) is asserted. Initial phase is fixed by \((A,0)\), and \(s=t/T(A)\) is normalized original physical time, not an orbital time-change. The associated conserved quantity is \(H(x,y)=(1+\kappa x^2)(1+\kappa y^2)\); its level through \((A,0)\) is \(Q\). The invariant curves \(H=Q>1\) are regular compact ovals, and the vector field is nonzero on them; hence each is a periodic orbit with a unique minimal period and the origin is the unique equilibrium.

## Proof
**1. Exact quarter-time density.** Direct differentiation gives \(\dot H=0\). Scale \(u=\sqrt\kappa x\), \(v=\sqrt\kappa y\) without changing time and write \(R=\sqrt\kappa A\). On the first clockwise quarter, \(u\) decreases from \(R\) to \(0\), and the energy identity gives
\[
\frac{dt}{|du|}=\frac1{\sqrt{(R^2-u^2)(1+u^2)}}.
\]
Introduce the logarithmic energy coordinate \(w=\log(1+u^2)/L\), where \(Q=1+R^2=e^L\). Algebraic substitution yields the *exact* time element
\[
|dt|=\frac{L}{2\sqrt Q}h_L(w)\,|dw|,\qquad
h_L(w)=g(Lw)g(L(1-w)),\qquad
g(z)=(1-e^{-z})^{-1/2}.
\]
The two endpoint singularities are integrable. Set
\[
I_L=\int_0^1h_L(w)\,dw,\qquad
F_L(w)=I_L^{-1}\int_0^w h_L(z)\,dz.
\]
The system commutes with the quarter-turn \((x,y)\mapsto(y,-x)\), so the four quarters take equal physical time. Therefore the exact minimal period is
\[
T(A)=\frac{2L}{\sqrt Q}I_L.
\]
On the first quarter the normalized elapsed quarter-time \(\tau=4s\in[0,1]\) satisfies \(\tau=1-F_L(w)\), hence \(U_A(s)=F_L^{-1}(1-4s)\) for \(0\le s\le1/4\). On successive quarters the logarithmic coordinate alternates by \(w\mapsto1-w\), yielding the stated triangular limit once \(F_L\) tends uniformly to the identity.

**2. Exact boundary mass.** For \(q(z)=g(z)-1\), \(q\) is positive and integrable: it behaves like \(z^{-1/2}\) at zero and decays exponentially at infinity. With \(r=\sqrt{1-e^{-z}}\),
\[
J:=\int_0^\infty q(z)\,dz
=\int_0^1\frac{2}{1+r}\,dr=2\log2.
\]
Use the decomposition
\[
h_L(w)-1=q(Lw)+q(L(1-w))+q(Lw)q(L(1-w)).\]
The first two integrals on \([0,1]\) each equal \(J/L+o(L^{-1})\). For the product, split the domain at \(1/2\). When \(w\le1/2\), the second factor is exponentially small in \(L\) and the first has integral \(O(L^{-1})\); the reversed bound applies for \(w\ge1/2\). Thus the product contributes \(o(L^{-1})\), proving
\[
I_L=1+\frac{2J}{L}+o(L^{-1})
=1+\frac{4\log2}{L}+o(L^{-1}).
\]
This gives the asserted period expansion. Also \(\sup_w|F_L(w)-w|=O(L^{-1})\): the absolute cumulative excess of \(h_L\) is at most \(I_L-1=O(L^{-1})\), and \(I_L\to1\). Consequently \(F_L^{-1}\to\mathrm{id}\) uniformly and the global triangle-profile convergence follows.

**3. The maximizer, with no unproved endpoint interchange.** Symmetry gives \(h_L(1-w)=h_L(w)\) and \(F_L(1-w)=1-F_L(w)\). Since
\[
(\log g)'(z)=-\frac1{2(e^z-1)}
\]
is strictly increasing in \(z>0\), \(h_L\) is strictly decreasing on \((0,1/2)\) and strictly increasing on \((1/2,1)\). The minimum at \(1/2\) is strictly less than the average \(I_L\), while \(h_L\) diverges at the endpoints. Thus there is exactly one \(w_L\in(0,1/2)\) such that \(h_L(w_L)=I_L\), and the other crossing is \(1-w_L\). The function \(F_L(w)-w\) attains its positive maximum at \(w_L\) and its negative minimum at \(1-w_L\).

Because \(I_L-1\sim2J/L\) while \(h_L(\delta)-1\) is exponentially small for every fixed \(0<\delta<1/2\), one has \(w_L\to0\). Since \(h_L(w_L)=I_L\to1\) but \(h_L(w_L)\ge g(Lw_L)\), necessarily \(Lw_L\to\infty\). We may now calculate the mass below the moving crossing, using the integrable decay of \(q\):
\[
\begin{split}
L\int_0^{w_L}(h_L(w)-1)\,dw&\longrightarrow J,\\
Lw_L(I_L-1)&\longrightarrow0.
\end{split}
\]
The term containing \(q(L(1-w))\) and the product term vanish exponentially on \([0,w_L]\). It follows that
\[
L\max_w(F_L(w)-w)=
\frac L{I_L}\left[\int_0^{w_L}(h_L-1)\,dw-w_L(I_L-1)\right]\longrightarrow J.
\]
For any increasing homeomorphism of \([0,1]\), the sup-norm distance to the identity equals that of its inverse, so the phase identity in step 1 and quarter-turn symmetry give
\[
L\|U_A-U_\infty\|_\infty\longrightarrow J=2\log2.
\]

**4. The sharp probability law.** Uniform normalized time on each quarter pushes forward under the log coordinate to the density \(f_L(w)=h_L(w)/I_L\), and all four quarters give that same law because of reflection symmetry. The region on which \(f_L(w)>1\) consists exactly of \((0,w_L)\cup(1-w_L,1)\). The equality of positive and negative variation gives the exact finite-\(L\) identity
\[
\begin{split}
d_{\mathrm{TV}}(\nu_A,\mathrm{Leb}_{[0,1]})
&=\frac12\int_0^1|f_L(w)-1|\,dw\\
&=2\,[F_L(w_L)-w_L].
\end{split}
\]
Multiplication by \(L\) and step 3 give the limit \(4\log2\). Finally, \(H=Q\) implies \(\log(1+\kappa x^2)+\log(1+\kappa y^2)=L\) at every time, proving the exact complement identity. All claims follow.

## Verification
The accompanying `CHECK.py` numerically evaluates the exact quarter-time integral, independently compares its period with the complete elliptic integral \(4K_{\mathrm{par}}(-\kappa A^2)\), and checks convergence of the boundary mass and finite-amplitude total variation. It is illustrative numerical corroboration only. The proof above is analytic for every \(\kappa>0\) and does not rely on finite sampling, numerical integration, or an unproved limit exchange. Run the auxiliary check with Python 3 and `mpmath` from `requirements.txt` via `python CHECK.py`.

## Relationship to prior work
The system is case (a) of Theorem 2 and equation (11) of Llibre--Rondón [1] after setting \(\kappa=-c_1>0\). That work classifies global centers; the existence of this one is therefore not a new claim. The earlier García-Saldaña--Llibre--Valls cubic classification [2] also addresses global-center conditions, not physical-time logarithmic energy-share distributions in the inspected theorem material. The period has the standard exact representation \(4K_{\mathrm{par}}(-\kappa A^2)\), where \(K_{\mathrm{par}}(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}\,d\theta\) uses the elliptic *parameter* convention, and its two-term expansion is an application of classical complete-elliptic-integral asymptotics [3]. The **new statement proposed here** is the uniform log-energy triangular phase law with sharp sup-norm defect and the sharp total-variation law for uniform physical-time sampling. Fixed-argument Jacobi-function degenerations [4] do not directly state these two global distributional constants.

## Limitations
The theorem concerns this exact cubic subfamily with \(\kappa>0\), not all cubic global centers; no perturbation robustness or full parameter-uniformity is claimed. The assertion is about asymptotically large amplitude and normalized physical phase, not a claim of a physical-time periodic orbit at infinite amplitude. Existing general elliptic-integral asymptotic theories could potentially recover some constants after further transformation; the cited literature comparison cannot establish absolute novelty. All originality assessments are limited to the specified inspected material.

## References
[1] J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1 (public 11 October 2023), Theorem 2(a), equation (11), https://arxiv.org/html/2310.07454v1.

[2] J. D. García-Saldaña, J. Llibre and C. Valls, *Linear type global centers of linear systems with cubic homogeneous nonlinearities*, Rend. Circ. Mat. Palermo (2019), DOI: 10.1007/s12215-019-00433-0, lawful author preprint https://ddd.uab.cat/pub/artpub/2019/221314/GarLliVal2018_Preprint.pdf.

[3] NIST Digital Library of Mathematical Functions, §19.12, *Asymptotic Approximations*, https://dlmf.nist.gov/19.12.

[4] NIST Digital Library of Mathematical Functions, §22.5, *Special Values*, https://dlmf.nist.gov/22.5.
