# Central-trinomial last-step extinction law for three-state excitation on paths

## Finding
For every integer \(n\ge2\), consider synchronous three-state Greenberg–Hastings dynamics on the finite path \(P_n\) with open (free) endpoints. Let \(\tau(x)\) be the first time that every vertex is resting, for initial state \(x\in\{0,1,2\}^n\). The sharp upper bound is \(\max_x\tau(x)=n+1\). Let \(N_n=|\{x:\tau(x)=n+1\}|\). If \(C_m\) is the central trinomial coefficient,
\[
C_m=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{j!^2(m-2j)!},\qquad m\ge0,
\]
then the exact last-step population is
\[
\boxed{N_n=C_{n-1}+C_{n-2}}.
\]
Its ordinary generating function and uniform-start asymptotic are
\[
\sum_{n\ge2}N_nz^n=z\left(\sqrt{\frac{1+z}{1-3z}}-1\right),\qquad
\frac{N_n}{3^n}\sim \frac{2}{3\sqrt{3\pi n}}.
\]
The square root denotes the unique formal power series with constant coefficient \(1\). The first populations, for \(n=2,3,\ldots,11\), are \(2,4,10,26,70,192,534,1500,4246,12092\).

## Assumptions and scope
The graph \(P_n\) has vertices \(0,\ldots,n-1\) and edges between consecutive integers, with no external neighbours or periodic wrap-around. The local states are resting \(0\), excited \(1\), refractory \(2\). At each integer time, an excited site becomes refractory, a refractory site becomes resting, and a resting site becomes excited if and only if at least one of its actual graph neighbours is excited. All sites update simultaneously. Counts distinguish vertex-labelled initial words; no quotient by reflection is taken. The only attractor is the all-resting fixed point.

## Proof
**1. Path-integral excitation invariant.** For an oriented edge \(u\to v\), put \(\delta(u,v)=\mathbf1_{\{x_u=0,x_v=1\}}-\mathbf1_{\{x_u=1,x_v=0\}}\). Let \(c_t(v)\) be the number of times vertex \(v\) has made a transition \(0\to1\) during the first \(t\) updates. The standard Greenberg–Hastings path-integral recurrence (see Gravner–Lyu–Sivakoff, Lemma 1) is
\[
c_{t+1}(v)=\max\left\{c_t(v),\max_{u\sim v}\big(c_t(u)+\delta(v,u)\big)\right\},\qquad c_0(v)=0.
\]
It gives \(c_t(v)\) as the maximum initial-colour integral over walks starting at \(v\) with at most \(t\) edges. On a tree, successive reverse traversals cancel in the integral; a walk can therefore be reduced to a simple path without changing its integral. Every simple path in \(P_n\) has at most \(D=n-1\) edges, whence \(c_t=c_D\) for \(t\ge D\). Thus there are no newly excited sites after physical time \(D\), and all sites are resting by \(D+2=n+1\).

**2. Exactly which initial words need the last update?** At time \(D\), some site is excited if and only if \(c_D(v)>c_{D-1}(v)\) for some vertex \(v\). Only the two endpoints have an opposite vertex at distance \(D\), so only endpoint events matter. Writing \(s_0=0\) and
\[
s_k=\sum_{i=0}^{k-1}\delta(i,i+1),\qquad 1\le k\le D,
\]
the left-endpoint event is precisely \(s_D>\max_{0\le k<D}s_k\). The right-endpoint event is \(s_0>\max_{1\le k\le D}s_k\). They are disjoint (the first has \(s_D>0\), the second \(s_D<0\)), and reflection gives equal populations. Reversal combined with exchanging symbols \(0\) and \(1\), keeping \(2\) unchanged, converts either event bijectively to the words for which **every nonempty forward prefix sum of edge increments is strictly positive**. Such words necessarily start with the pair \(01\). Consequently the desired count equals twice the number of positive-prefix continuations of the word \(01\).

**3. Exact nonnegative-height generating function.** Let \(Q_h^a(z)\) be the length-generating series of all allowable continuations from present letter \(a\in\{0,1,2\}\) at prefix height \(h\ge1\), never hitting zero, counting the empty continuation. A new letter contributes a factor \(z\). With boundary \(Q_0^0(z)=0\), the three recurrences are
\[
\begin{aligned}
Q_h^0&=1+z(Q_h^0+Q_{h+1}^1+Q_h^2),\\
Q_h^1&=1+z(Q_{h-1}^0+Q_h^1+Q_h^2),\\
Q_h^2&=1+z(Q_h^0+Q_h^1+Q_h^2).
\end{aligned}
\]
The constant-in-height bulk solution is \(U=(1-3z)^{-1}\). Subtracting \(U\) and looking for a homogeneous correction proportional to \(\rho^{h-1}\) yields the kernel
\[
z^3\rho^2-(1-3z+2z^3)\rho+z^3=0.
\]
There is exactly one root \(\rho\in z^3\mathbb Q[[z]]\); the other root is Laurent, so it is excluded by coefficientwise boundedness as \(h\to\infty\). Apply the boundary \(Q_0^0=0\), solve the resulting linear system for the three correction coefficients, and simplify the quadratic discriminant using \(1-3z+4z^3=(1+z)(1-2z)^2\). This gives
\[
Q_1^1(z)=\frac{1}{2z}\left(\sqrt{\frac{1+z}{1-3z}}-1\right).
\]
There are \(n-2\) further letters after the forced prefix \(01\). Therefore \(N_n=2[z^{n-2}]Q_1^1(z)\), establishing the asserted generating function.

**4. Trinomial identity and asymptotic.** The classical constant-term count of \((w^{-1}+1+w)^m\) has generating function
\[
\sum_{m\ge0}C_mz^m=\frac{1}{\sqrt{1-2z-3z^2}}.
\]
Since \(1-2z-3z^2=(1+z)(1-3z)\), the last-step generating function is also \(z((1+z)\sum_{m\ge0}C_mz^m-1)\). Extracting its coefficient at \(z^n\) proves \(N_n=C_{n-1}+C_{n-2}\). Near the unique dominant singularity \(z=1/3\), the generating function has singular part \(2(1-3z)^{-1/2}/(3\sqrt3)\). The standard binomial-coefficient asymptotic then proves the stated probability law. The \(01\) prefix (or its reflection) shows \(N_n>0\) for all \(n\ge2\), so the upper bound is attained.

## Verification
The companion `verify.py` independently implements the synchronous local update and exhaustively checks all \(3^n\) initial conditions for every \(2\le n\le11\), including the universal upper bound. A separate positive-prefix dynamic program and an algebraic generating-function recurrence are cross-checked against the central-trinomial formula for every \(2\le n\le42\). The saved `verification_output.txt` records the counts and the success marker. Finite checks corroborate but do not replace the arbitrary-\(n\) proof.

## Relationship to prior work
Durrett and Steif (1991), Section 2, relate one-dimensional excited-site survival to strict ballot events and derive a large-time probability asymptotic for an infinite line; their Section 5 treats higher-dimensional finite periodic boxes. Fisch and Gravner (1995) study one-dimensional Greenberg–Hastings dynamics and infinite-line pulse decay. Gravner, Lyu and Sivakoff (2016) supply the general max-plus path-integral lemma. These results motivate the endpoint criterion, but the inspected material does not report the exact population \(C_{n-1}+C_{n-2}\) for the open finite path's sharp global extinction time. The new statement is an exact finite-volume enumeration, not a claim that the ballot mechanism or the decay exponent is new.

## Limitations
Only open paths, uniform three-state transition rules and the single maximal extinction-time stratum are counted. The theorem gives neither a complete distribution of all transient depths nor a claim of historical uniqueness. Previously unknown equivalent finite-volume counts, possibly implicit in general ballot-enumeration literature, remain an originality risk. The computations are finite checks; the infinite-family claim rests on the path-integral and generating-function arguments.

## References
1. R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability 4 (1991), 669–690. https://sites.math.duke.edu/~rtd/reprints/paper66.pdf
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016). https://arxiv.org/abs/1610.07320
4. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv posting March 22, 1993, arXiv:patt-sol/9303002. https://arxiv.org/abs/patt-sol/9303002
