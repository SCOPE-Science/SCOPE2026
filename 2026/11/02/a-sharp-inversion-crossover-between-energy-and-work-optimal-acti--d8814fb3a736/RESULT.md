# A sharp inversion crossover between energy- and work-optimal active batteries

## Finding

For the stationary two-state active-battery model at any fixed inverse temperature \(\beta>0\) and positive active affinity \(a>0\), allow its excited-level energy \(E>0\) to vary across battery designs while \(a\) and \(\beta\) stay fixed. Write \(b=\beta a\), \(z=\beta E\), and set
\[
 p_b(z)=\frac{1}{1+e^{z-b}},\qquad q(z)=\frac{1}{1+e^z}.
\]
Two distinct natural stationary objectives are the dimensionless *recoverable free-energy capacity*
\[
 C_b(z)=D_{\mathrm{KL}}(\mathrm{Bern}(p_b(z))\|\mathrm{Bern}(q(z)))
\]
and the *excess mean internal energy*
\[
 U_b(z)=z[p_b(z)-q(z)].
\]
Both have unique global maximizers \(z_C(b)\) and \(z_U(b)\) on \(z>0\), with
\[
 \boxed{z_C(b)=\log\!\left[\frac{e^b(e^b-1-b)}{e^b(b-1)+1}\right]},
 \qquad \boxed{\frac b2<z_C(b)<\min\{b,z_U(b)\}}.
\]
The other optimum \(z_U(b)>b/2\) is the unique solution of
\[
 \boxed{\frac{z_U(b)}2\left[\tanh\!\left(\frac{z_U(b)}2\right)-
 \tanh\!\left(\frac{b-z_U(b)}2\right)\right]=1}.
\]
There is exactly one \(b_c>0\) such that
\[
 \boxed{\frac{b_c}{2}\tanh\!\left(\frac{b_c}{2}\right)=1},
 \qquad b_c=2.3993572805154676678\ldots.
\]
For \(0<b<b_c\), the internal-energy-optimal excited state is *not population inverted*, since \(z_U(b)>b\); at \(b=b_c\) it is exactly at the inversion boundary, and for \(b>b_c\) it is inverted, with \(z_U(b)<b\). In contrast, the recoverable-work optimum obeys \(z_C(b)<b\) and is population inverted for every \(b>0\). Moreover, if \(z_0>0\) is the unique root of \(z_0\tanh(z_0/2)=1\), then
\[
 z_C(b)/b\longrightarrow\frac23,\qquad z_U(b)\longrightarrow z_0=1.5434046384182084\ldots,
\]
\[
 \boxed{\lim_{b\downarrow0}\frac{C_b(z_U(b))}{C_b(z_C(b))}
 =\operatorname{sech}^2(z_0/2)=0.5802019684911432\ldots}.
\]
Thus designing for excess internal energy instead of extractable nonequilibrium free energy loses asymptotically approximately \(41.98\%\) of the maximum recoverable capacity in the weak-affinity limit.

## Assumptions and scope

The model is a two-state system with lower energy zero and excited energy \(E>0\), an equilibrium thermal reference at inverse temperature \(\beta>0\), and a fixed coarse-grained active affinity \(a>0\) satisfying local detailed balance \(\log(k_{01}/k_{10})=\beta(a-E)\). The state has reached its stationary affinity-biased occupation \(p_b(z)\), while its uncharged reference occupation is \(q(z)\). The activity, temperature and kinetic gating convention are held fixed when \(E\) is varied across designs. The tested objectives are energy \(E[p_b-q]\) and excess nonequilibrium free energy \(\beta^{-1}C_b(z)\), *not* ergotropy of an isolated quantum qubit, output charging power, a net efficiency including reservoir maintenance, or total manufacturing cost. The inversion criterion is the charged-state condition \(p_b(z)>1/2\), equivalent to \(z<b\). All maxima are taken over the entire open domain \(z>0\), and all quantified statements hold for every \(b>0\).

## Proof

Set \(k=e^b>1\), \(u=e^z>1\), \(p=k/(k+u)\), and \(q=1/(1+u)\). Their positive difference is
\[
 \Delta=p-q=\frac{u(k-1)}{(u+1)(u+k)}=
 \frac{\sinh(b/2)}{2\cosh(z/2)\cosh((b-z)/2)}>0.
\]
The identity \(\log[p/(1-p)]-\log[q/(1-q)]=b\) gives, by differentiating the Bernoulli relative entropy and using \(p'=-p(1-p)\),
\[
 C'_b(z)=\Delta-bp(1-p)
 =\frac{u\{k(k-1-b)-[k(b-1)+1]u\}}{(u+1)(u+k)^2}.
\]
Both \(k-1-b>0\) and \(k(b-1)+1>0\): the first follows from \(e^b>1+b\), and the second from \(e^b(b-1)+1=\int_0^b t e^t\,dt>0\). Hence \(C'_b\) has precisely one zero on \(u>0\), with derivative positive below the root and negative above it. This root satisfies \(u=e^{z_C}\) as stated. To see that it falls in the physical domain and within the affinity, direct substitution yields
\[
 C'_b(b/2)=\frac{2\sinh(b/2)-b}{4\cosh^2(b/4)}>0,
 \qquad C'_b(b)=\frac{2\tanh(b/2)-b}{4}<0.
\]
Thus \(b/2<z_C<b\); in particular it is the unique global capacity maximizer in \(z>0\). Also \(C_b(z)>0\) for each finite \(z>0\), while \(C_b(z)\to0\) as \(z\to\infty\).

Next define
\[
 H_b(z)=\frac z2\left[\tanh(z/2)-\tanh((b-z)/2)\right].
\]
Taking the logarithmic derivative of the hyperbolic expression for \(\Delta\) gives
\[
 U'_b(z)=\Delta(z)[1-H_b(z)].
\]
For \(0<z\le b/2\), \(H_b(z)\le0\). For \(z>b/2\), both the bracket and its derivative \([\operatorname{sech}^2(z/2)+\operatorname{sech}^2((b-z)/2)]/2\) are strictly positive; therefore \(H_b\) is strictly increasing there, from zero to infinity. Consequently \(U'_b\) switches sign exactly once at \(H_b(z_U)=1\), proving uniqueness and global maximality (\(U_b(z)\to0\) at infinity).

At \(z=z_C\), the capacity stationarity equation is \(\Delta=bp(1-p)\). It follows that
\[
 U'_b(z_C)=\Delta-z_C[p(1-p)-q(1-q)]
 =(b-z_C)p(1-p)+z_C q(1-q)>0.
\]
The unique zero of \(U'_b\) therefore satisfies \(z_U>z_C\). At \(z=b\), the expression for \(H_b\) simplifies to \(H_b(b)=b\tanh(b/2)/2\). This is strictly increasing from zero to infinity as \(b\) increases from zero to infinity; its single level-one crossing is \(b_c\). Since \(H_b\) is strictly increasing above \(b/2\), \(H_b(b)<,=,>1\) respectively entails \(z_U>b\), \(z_U=b\), \(z_U<b\). This proves the sharp inversion phase diagram.

For weak affinity, elementary Taylor expansion of the explicit expression for \(z_C\) gives \(z_C/b\to2/3\). Also \(H_b(z)\to z\tanh(z/2)\) locally uniformly on \(z>0\); strict monotonicity and root bracketing imply \(z_U\to z_0\), the unique positive level-one solution. At fixed \(z\), the charged and thermal Bernoulli populations differ by \(bq(1-q)+O(b^2)\), so a second-order relative-entropy expansion yields
\[
 C_b(z)=\frac{b^2}{2}q(z)[1-q(z)]+O(b^3)
 =\frac{b^2}{8\cosh^2(z/2)}+O(b^3)
\]
uniformly on compact \(z\)-sets containing the limits of both optimizing sequences. Substitution at \(z_C\to0\) and \(z_U\to z_0\) gives the stated ratio. All these statements follow from exact finite-dimensional identities; no stochastic simulation or limiting numerical experiment is used as proof.

## Verification

The accompanying stand-alone Python script `check_design.py` uses `sympy` for symbolic derivative identities and `mpmath` for high-precision bracketing, optimizer signs, and critical limits. The actual saved script completed 3,000 assertions and reports \(b_c=2.3993572805154676678\ldots\), \(z_0=1.5434046384182084479\ldots\), and the relative-capacity fraction \(0.5802019684911432368\ldots\). These finite checks only supplement the analytic argument, which establishes the infinite ranges of \(b\) and \(z\).

To reproduce: run `python check_design.py` with Python 3 and the `sympy` and `mpmath` packages installed. No external data files are required.

## Relationship to prior work

Lin, Liu, and Ma [1] introduce exactly the two-state charged and thermal occupations used here and identify recoverable capacity with Bernoulli relative entropy, including a detailed charging-time and power-efficiency analysis. Their main text and Appendices A–C do not state a global maximization over the *design gap* at fixed affinity, compare excess mean energy with free-energy capacity as different objectives, or identify the inversion threshold at \(b_c\). All of their model equations and thermodynamic meanings are credited, rather than claimed as new. Lei and coauthors [2] optimize passive resistor–capacitor charging time, power, and multi-stage current protocols, not this energy-level design problem. The associated discharging study [3] treats finite-time output protocols, not the stationary gap choices here. The new claim is precisely the complete two-objective design classification, sharp inversion transition, and limiting capacity-loss constant. The result can be derived from the source's pointwise stationary formulas by substantial optimization, so independent bibliographic priority remains to be established.

## Limitations

The theorem is a stationarity-and-design result only. It does not account for variation of the active affinity as the microscopic energy landscape changes, constraints on the tunable gap, energy consumed in manufacturing or tuning that gap, or reservoir housekeeping dissipation. It does not optimize finite charging durations or work recovery protocols. A general relative-entropy theorem or a separate, unindexed battery-design analysis might already imply some conclusions; these searches and explicit source comparisons are evidence of provisional best-knowledge originality, not proof of novelty. No independent audit has been performed.

## References

- Y.-Q. Lin, R.-H. Liu, and Y.-H. Ma, *Active-Matter Battery*, arXiv:2610.00428v1 (first public version, 2026-09-30), https://arxiv.org/html/2610.00428v1. See main text, equations (1), (3), (4), and Appendix A–C.
- J.-R. Lei, Y.-Q. Lin, S.-G. Ou, and Y.-H. Ma, *Universal power-efficiency trade-off in battery charging*, Frontiers of Physics **20**, 042202 (2025), https://doi.org/10.15302/frontphys.2025.042202.
- R.-H. Liu, Y.-Q. Lin, and Y.-H. Ma, *Finite-time thermodynamics of battery discharging: power–efficiency trade-off and optimization*, Entropy **28**, 852 (2026), https://doi.org/10.3390/e28080852.
