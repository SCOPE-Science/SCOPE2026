# Exact cancellation removes the predator-harvest stability threshold
## Finding
Consider the semi-trivial periodic orbit in Xu and Zou's weighted-harvesting predator-prey model with \(\tau_l=0\) and \(y(t)\equiv0\). Under the finite-cycle assumptions \(r,\mu,K,h_l,E_l,p_1,p_2>0\), \(0<\eta<1\), \(h_l<\eta K\), \(0<p_1E_l<1\), and \(0<p_2E_l<1\), write
\[
x_0=\frac{(1-p_1E_l)h_l}{\eta},\qquad x_T=\frac{h_l}{\eta}.
\]
The source gives the convergence ratio
\[
\rho_1=(1-p_2E_l)\frac{\eta K-(1-p_1E_l)h_l}{\eta K-h_l}
\exp\!\left(\int_0^T\left(-\frac{r x(t)}{K}-\mu\right)dt\right).
\]
This ratio simplifies exactly to
\[
\boxed{\rho_1=(1-p_2E_l)e^{-\mu T}}.
\]
Therefore \(0<\rho_1<1\) for every admissible \(p_2\). The quantity
\[
\bar p_2=\frac{p_1h_l}{\eta K-(1-p_1E_l)h_l}
\]
is a sufficient-condition artifact, not a stability threshold for this semi-trivial orbit. In particular, the paper's subsequent implication \(p_2<\bar p_2\Rightarrow\rho_1>1\) is false.

## Assumptions and scope
The continuous dynamics are
\[
\dot x=rx\left(1-\frac{x}{K}\right)-\frac{axy}{1+aqx},\qquad
\dot y=e\psi(y)\frac{axy}{1+aqx}-\mu y,
\]
with \(\psi(0)=0\). Harvesting occurs when \(\eta x+(1-\eta)y=h_l\), with jumps \(\Delta x=-p_1E_lx\) and, when \(\tau_l=0\), \(\Delta y=-p_2E_ly\). On \(y=0\), the prey therefore follows the logistic equation and the predator linearization between impulses has coefficient \(-\mu\).

The strict inequality \(h_l<\eta K\) is imposed so that the source's displayed flight time is finite. The reset condition \(0<p_1E_l<1\) keeps \(x_0\) strictly between zero and \(x_T\), and \(0<p_2E_l<1\) is the source's positive post-harvest predator condition. No claim is made here about the boundary \(h_l=\eta K\), about \(\tau_l>0\), or about positive periodic solutions.

## Proof
Set
\[
A=\eta K-(1-p_1E_l)h_l,\qquad B=\eta K-h_l.
\]
Then \(K-x_0=A/\eta\) and \(K-x_T=B/\eta\). Along the logistic flight,
\[
\frac{d}{dt}\log(K-x(t))
=-\frac{\dot x(t)}{K-x(t)}
=-\frac{r x(t)}{K}.
\]
Hence
\[
\exp\!\left(\int_0^T-\frac{r x(t)}{K}\,dt\right)
=\frac{K-x_T}{K-x_0}
=\frac{B}{A}.
\]
Substitution into the source's convergence-ratio formula gives
\[
\rho_1=(1-p_2E_l)\frac{A}{B}\frac{B}{A}e^{-\mu T}
=(1-p_2E_l)e^{-\mu T}.
\]
The source's flight time is
\[
T=\frac1r\log\!\left(\frac{A}{(1-p_1E_l)B}\right).
\]
Because
\[
A-(1-p_1E_l)B=\eta Kp_1E_l>0,
\]
we have \(T>0\). Since also \(0<1-p_2E_l<1\) and \(\mu>0\), it follows that \(0<\rho_1<1\). The standard state-dependent impulsive stability criterion used by the source therefore certifies orbital asymptotic stability throughout the admissible \(p_2\)-range.

For an exact witness, choose
\[
r=2,\quad K=100,\quad \mu=1,\quad \eta=\frac35,\quad h_l=30,\quad
p_1=\frac3{10},\quad E_l=2,\quad p_2=\frac1{10}.
\]
Then \(A=48\), \(B=30\), \(1-p_1E_l=2/5\), and
\[
T=\frac12\log\!\left(\frac{48}{(2/5)30}\right)=\log 2.
\]
Moreover
\[
\bar p_2=\frac{(3/10)30}{48}=\frac3{16},\qquad
p_2=\frac1{10}<\frac3{16},
\]
yet
\[
\rho_1=\left(1-\frac15\right)e^{-\log2}=\frac25<1.
\]
This directly contradicts the printed instability implication below the proposed threshold.

## Verification
The standalone verifier `verification/verifier.py` checks the exact rational identities in the witness, including \(A=48\), \(B=30\), the flight-time logarithm argument \(4\), \(\bar p_2=3/16\), and the final multiplier \(\rho_1=2/5\). Running `python3 verification/verifier.py` returns `VERIFY_OK`.

The proof itself is symbolic and does not depend on finite enumeration or floating-point evidence. The only external dynamical ingredient is the standard orbital-stability criterion for state-dependent impulsive planar systems; the 2026 source applies that criterion to derive the displayed \(\rho_1\), and the 2023 weighted-fishing predecessor states the same criterion explicitly.

## Relationship to prior work
Xu and Zou derive the unsimplified \(\rho_1\), observe that their inequality \(p_2>\bar p_2\) is only sufficient because of exponential attenuation, but then assert that \(p_2<\bar p_2\) makes \(\rho_1>1\). The exact logistic identity above evaluates that attenuation term completely and shows that it cancels the geometric factor. Thus the source's sufficient statement remains true but is non-sharp; the opposite-side instability assertion fails.

The closest inspected weighted-fishing predecessor, Tian, Gao, and Sun (2023), uses predator dynamics whose linear coefficient at \(y=0\) depends on the prey state. It therefore does not imply the cancellation \(\rho_1=(1-p_2E_l)e^{-\mu T}\). Xu and Zou themselves distinguish their model from earlier weighted-escapement work by the general predator Allee effect with \(\psi(0)=0\). A 2022 predecessor also studies stability thresholds for predator-extinction periodic solutions under weighted escapement, but only its abstract and bibliographic record were inspected here; the 2026 source describes that earlier framework as lacking the general predator Allee mechanism. No correction or erratum for the 2026 threshold statement was found in the checked sources.

## Limitations
This result addresses only the semi-trivial periodic orbit with \(\tau_l=0\) and a finite logistic flight. It does not classify positive periodic solutions, and it does not prove that the existence conclusion of Theorem 2.2 is false. It does show that the proof of case (1) in that theorem begins from a semi-trivial-instability premise that fails under the stated finite-cycle assumptions, so that downstream argument requires a different justification.

The literature check cannot establish absolute uniqueness. The 2022 weighted-escapement predecessor was not inspected in full text, leaving a residual possibility that a formally similar cancellation was noticed in a different model. That risk does not cover the present claim: the inspected 2026 source presents the exact formula and threshold assertion corrected here, and its own literature discussion says the earlier weighted-escapement models did not include the general predator Allee effect used in this simplification.

## References
J. Xu and T. Zou, “Dynamics of a predator-prey model with the Allee effect for the predator induced by weighted harvesting strategy,” AIMS Mathematics 11(1) (2026), 578–593. DOI: 10.3934/math.2026025.

Y. Tian, Y. Gao, and K. Sun, “A fishery predator-prey model with anti-predator behavior and complex dynamics induced by weighted fishing strategies,” Mathematical Biosciences and Engineering 20(2) (2023), 1558–1579. DOI: 10.3934/mbe.2023071.

Y. Tian, Y. Gao, and K. Sun, “Global dynamics analysis of instantaneous harvest fishery model guided by weighted escapement strategy,” Chaos, Solitons & Fractals 164 (2022), 112597. DOI: 10.1016/j.chaos.2022.112597.
