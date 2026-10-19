# A rare-noise Bessel crossover for monitored quantum-stochastic first returns

## Finding

Consider the discrete-time quantum-stochastic walk of Štefaňák, Potoček, Yalçınkaya, Gábris and Jex, on the integer line with the exchange coin \(\theta=\pi/2\). Let \(p\in[0,1]\) be the probability of a classical shift at each step, let \(T_p\) be the first **monitored return to position zero**, and let \(S_m(p)=\Pr(T_p>m)\). A measurement is made after every step and the process is killed on detection. The initial position is zero and its coin state is arbitrary.

**Theorem (rare-noise first-return transition).** For every integer \(n\ge0\),
\[
S_{2n}(p)=S_{2n+1}(p)
=[z^{2n}]\sqrt{\frac{1-(1-2p)z}{1-z}},

\]
where \([z^{2n}]\) denotes ordinary Taylor-coefficient extraction about the origin. The generating-function identity follows from the known matrix first-return function in the originating work and is **not claimed as new**. Its sharp singular and joint-limit consequences are:

1. At \(p=0\), \(T_0=2\) almost surely. For every fixed \(0<p\le1\), \(\Pr(T_p<\infty)=1\) but \(\mathbb E T_p=\infty\), and
\[
S_{2n}(p)\sim\frac{\sqrt p}{\sqrt{\pi n}},\qquad
\Pr(T_p=2n)\sim\frac{\sqrt p}{2\sqrt\pi\,n^{3/2}}
\quad(n\to\infty).

\]
The already known fact of almost-sure recurrence is included only to specify the transition; the fixed-parameter tail and expectation conclusions are analyzed here.

2. For any sequence \(p\downarrow0\), \(n=n(p)\ge1\) with \(2np\to t\in[0,\infty)\), the following limit holds **uniformly when \(2np\) remains in a bounded interval**:
\[
\frac{S_{2n}(p)}p\longrightarrow
\Phi(t):=e^{-t}\bigl(I_0(t)+I_1(t)\bigr),

\]
where \(I_0,I_1\) are the modified Bessel functions of the first kind. In particular, conditioning on the event that the initial two-step return failed,
\[
pT_p\ \big|\ \{T_p>2\}\ \xrightarrow{\mathrm d}\ Z,
\qquad \Pr(Z>t)=\Phi(t)\quad(t\ge0).

\]
The limit law has density
\[
\frac{e^{-t}I_1(t)}t\quad(t>0),

\]
continuously extended to the value \(1/2\) at zero, and the algebraic far tail
\[
\Phi(t)\sim\sqrt{\frac{2}{\pi t}}\quad(t\to\infty).

\]
Thus the rare noise creates survivors of probability order \(p\) and delays their eventual return on the time scale \(p^{-1}\), with an explicit nonexponential limiting law.

## Assumptions and scope

The Hilbert space is \(\mathbb C^2\otimes\ell^2(\mathbb Z)\). The coin exchanges the basis states \(R,L\), and conditional translation shifts \(R\) right and \(L\) left. One step applies the coherent coined shift with probability \(1-p\), the identity-coin right shift with probability \(p/2\), and the identity-coin left shift with probability \(p/2\), as a convex mixture of three Kraus operations. The coin starts in an arbitrary normalized density state localized at position zero. At each strictly positive integer time, the position-zero projector is measured; the walk stops on a positive outcome, and the orthogonal projection is applied on a negative outcome. Consequently \(T_p\in\{2,4,6,\ldots\}\cup\{\infty\}\). The result is for this precisely specified coin endpoint, not arbitrary coin angles or alternative definitions of unmonitored recurrence.

At this coin endpoint the three Kraus steps are permutations of the position/coin basis: \((R,x)\mapsto(L,x-1)\) and \((L,x)\mapsto(R,x+1)\) with probability \(1-p\), or \((c,x)\mapsto(c,x\pm1)\) with probability \(p/2\) each. Orthogonality of the coin basis under every trajectory and parity/reflection symmetry make the observed first-return law independent of the initial coin density state. This is a classical two-internal-state process, while retaining its origin in a monitored quantum-stochastic channel.

## Proof

**Step 1: extract survival from the established first-return resolvent.** For a formal variable \(z\) about zero put
\[
a=1-(1-p)z,\quad b=1+(1-p)z,\quad c=pz,\quad
u=\sqrt{a^2-c^2},\quad v=\sqrt{b^2-c^2},
\]
with both square roots having constant term one. Appendix E, equations (72)–(75), of the originating paper computes the reduced return Green matrix \(G(z)\) and gives
\[
G(z)^{-1}=\frac12
\begin{pmatrix}
 av+bu&cu-cv\\ cu-cv&av+bu
\end{pmatrix}.
\]
The first-return matrix is \(F(z)=I-G(z)^{-1}\) by the monitored renewal identity. Every row sum is equal, so for any initial coin probability vector the scalar first-return generating function is
\[
f_p(z)=1-\frac12\bigl[(a-c)v+(b+c)u\bigr]
=1-\frac12\bigl[(1-z)v+(1+z)u\bigr].
\]
Consequently,
\[
u=\sqrt{(1-z)(1-(1-2p)z)},\qquad
v=\sqrt{(1+z)(1+(1-2p)z)}.
\]
Define \(H_p(z)=u/(1-z)=\sqrt{[1-(1-2p)z]/(1-z)}\). Since \(v/(1+z)=H_p(-z)\), the discrete renewal relation \(\sum_{m\ge0}S_m(p)z^m=[1-f_p(z)]/(1-z)\) simplifies exactly to
\[
\sum_{m\ge0}S_m(p)z^m
=\frac{1+z}{2}\bigl[H_p(z)+H_p(-z)\bigr].

\]
Comparing coefficients proves (1), including parity. Equivalently, if \(A_p(w)=\sum_{n\ge0}S_{2n}(p)w^n\), then
\[
A_p(w)=\tfrac12[H_p(\sqrt w)+H_p(-\sqrt w)],
\qquad \sum_{n\ge1}\Pr(T_p=2n)w^n=1-(1-w)A_p(w).

\]
These are identities of analytic germs at zero; the even combination is independent of the choice of square root. The case \(p=0\) gives \(H_0\equiv1\), hence \(S_0=S_1=1\) and \(S_m=0\) for \(m\ge2\).

**Step 2: fixed positive noise has a recurrent infinite-mean tail.** Fix \(0<p\le1\). Near \(z=1\),
\[
H_p(z)=\sqrt{2p}\,(1-z)^{-1/2}[1+O(1-z)].
\]
The even-series representation (8), using \(1-\sqrt w\sim(1-w)/2\), yields
\[
A_p(w)=\sqrt p\,(1-w)^{-1/2}+O(1)
\]
with a full local Puiseux expansion. For \(0<p<1\), the other branch point \(z=1/(1-2p)\), when finite, lies strictly outside the unit circle. At \(p=1\), the branch at \(z=-1\) contributes only less singular terms in the even combination; the same leading expansion holds. Singularity transfer on the slit plane gives
\[
[w^n]A_p(w)=\frac{\sqrt p}{\sqrt{\pi n}}+O_p(n^{-3/2}).
\]
Similarly (8) and coefficient transfer of \(-(1-w)^{1/2}\) give
\[
[w^n]\bigl[1-(1-w)A_p(w)\bigr]
=\frac{\sqrt p}{2\sqrt\pi\,n^{3/2}}+O_p(n^{-5/2}).
\]
This proves both expressions in (2). The positive-coefficient generating function tends to zero survival, so return probability is one. But
\[
\mathbb E T_p=\sum_{m\ge0}S_m(p)=2\sum_{n\ge0}S_{2n}(p)=\infty
\]
for each \(p>0\), in contrast with \(\mathbb E T_0=2\). There is no assertion of a uniform remainder as \(p\downarrow0\).

**Step 3: joint small-noise/long-time limit.** A formal binomial expansion gives, for every \(N\ge1\),
\[
[z^N]H_p(z)=
\sum_{k=1}^{N}{\binom{1/2}{k}}(2p)^k
\binom{N-1}{k-1}.

\]
Let \(N=2n\ge2\) and assume \(Np\to t\). Dividing (9) by \(p\) yields termwise convergence to
\[
\Psi(t):=\sum_{k=1}^{\infty}
\binom{1/2}{k}\frac{2^k t^{k-1}}{(k-1)!}.

\]
Indeed \(\binom{N-1}{k-1}\le N^{k-1}/(k-1)!\); when \(Np\le M\) the absolute value of the \(k\)-th summand after division by \(p\) is at most
\[
\left|\binom{1/2}{k}\right|\frac{2^k M^{k-1}}{(k-1)!},
\]
whose sum is finite for every \(M<\infty\). Thus dominated convergence is uniform on compact time-scale intervals, even at \(t=0\) for \(n\ge1\).

**Step 4: identify the scaling function and the conditional law.** The series (10) is entire. For sufficiently large \(s>0\), termwise integration yields
\[
\int_0^\infty e^{-st}\Psi(t)\,dt
=\sum_{k\ge1}\binom{1/2}{k}\left(\frac2s\right)^k
=\sqrt{1+\frac2s}-1.

\]
The standard elementary Laplace transforms of \(I_0\) and \(I_1\) show independently that
\[
\int_0^\infty e^{-st}e^{-t}[I_0(t)+I_1(t)]\,dt
=\sqrt{1+\frac2s}-1.
\]
Uniqueness of Laplace transforms (or equality of convergent Taylor series at zero) gives \(\Psi(t)=\Phi(t)\), proving (3). The exact two-step survival is
\[
S_2(p)=p-\frac{p^2}{2}.
\]
For fixed \(t>0\), choose \(n(p)=\lfloor t/(2p)\rfloor\) and use parity to obtain
\[
\Pr(pT_p>t\mid T_p>2)
=\frac{S_{2n(p)}(p)}{S_2(p)}\longrightarrow\Phi(t).
\]
At \(t=0\), both tails equal one. Bessel recurrences \(I_0'=I_1\), \(I_1'=I_0-I_1/t\) give
\[
-\Phi'(t)=\frac{e^{-t}I_1(t)}t>0\quad(t>0).
\]
Since \(\Phi(0)=1\), \(\Phi(\infty)=0\), this is a probability density; its origin limit is \(1/2\). Finally the standard large-argument asymptotic \(I_\nu(t)\sim e^t/\sqrt{2\pi t}\) yields (6). The limiting density is not an exponential distribution, and its survival has an infinite mean, consistent with the fixed-\(p\) tail.

## Verification

An independent executable checker, `rare_noise_return_check.py` (Python 3; dependency `mpmath>=1.3`), reproduces 215 assertions: (i) exact rational propagation of the killed position/coin walk over finite horizons, compared to the power series in (1); (ii) Fourier integration of the independent two-state return resolvent, compared with the expression in Step 1; (iii) evaluations of the joint scaling curve and its Bessel derivative; and (iv) large-time fixed-\(p\) coefficient ratios. It runs as `python rare_noise_return_check.py` after installing `mpmath>=1.3` (see `requirements.txt`). Finite computations are checks, not a replacement for singularity transfer, dominated convergence, or Laplace uniqueness in the proof.

## Relationship to prior work

Štefaňák et al. (2025 preprint; 2026 journal) define the monitored model and obtain its return Green function and first-return matrix, particularly equations (67)–(79) in Appendix E. They prove that the \(\theta=\pi/2\) model has return probability one for all classical-step probabilities and discuss the failure of a finite-horizon derivative to converge uniformly as noise vanishes. **These model definitions, the complete Green and first-return generating functions, and recurrence probability one are existing work, not original claims here.** Equations (1), (7), (8), and the first-return generating function are straightforward reorganizations of their formulas, used solely as premises. The additional assessed result is the specific singular-return asymptotics, the abrupt infinite-mean threshold, and the explicit **conditional joint small-noise/long-time scaling limit** (3)–(6), which requires analyzing simultaneously a vanishing mixing probability and a diverging horizon.

Konno (2009) studies correlated random walks, including Bessel-function rare-switching limits of the *position distribution* and one- and two-boundary absorption for a persistent-direction model. In that model the internal state tracks the last movement direction; in the present mixed quantum/classical channel a classical shift may move opposite to the unchanged coin, so the finite transition matrices are different. Neither its position limit nor its boundary absorption probability states the present first-return conditional distribution. Kiumi–Konno–Tamura (2022) study position-return probabilities of quantum and correlated walks without the same per-step killing; return at a chosen observation time is not the first detected return. Yoshino et al. (2025) analyze position limit distributions for a different quantum/persistent-walk interpolation and separately discuss a rare-noise scaling \(p\propto1/n\); their observable and channel are different and they do not establish this monitored first-hitting Bessel survival law. Classical persistent-walk/telegraph first-passage theory contains related Bessel functions, creating a residual risk of an implicit more general derivation. The known exact generating function in Štefaňák et al. also determines all finite-time survival probabilities, so the present contribution is a **new analyzed asymptotic regime**, not additional information at fixed parameters beyond that generating function.

## Limitations

The theorem is at the exactly exchanging coin endpoint and requires position monitoring after every step. At generic coins, coherent interference prevents the same two-state Markov reduction. The results concern population first-return statistics, not unmonitored return probabilities or quantum-state return to the initial coin. The fixed-positive-\(p\) large-time asymptotic is not claimed uniform in \(p\) near zero; the joint limit fills one distinguished boundary layer. No finite-sample estimation, non-Markovian environmental noise, or higher-dimensional lattice extension is claimed. Potential derivability of the joint law from more general persistent-walk theory remains a literature risk; independent audit has not been performed.

## References

1. M. Štefaňák, V. Potoček, İ. Yalçınkaya, A. Gábris, I. Jex, *Recurrence in discrete-time quantum stochastic walks*, arXiv:2501.08674v1 (first posted 2025-01-15), later *Quantum* **10**, 1982 (2026), DOI:10.22331/q-2026-01-22-1982. Open full text: https://quantum-journal.org/papers/q-2026-01-22-1982/pdf/ . Appendix E, equations (67)–(79).
2. C. Kiumi, N. Konno, S. Tamura, *Return Probability of Quantum and Correlated Random Walks*, *Entropy* **24**, 584 (2022), DOI:10.3390/e24050584; arXiv:2203.07674.
3. S. Yoshino, H. Shiratori, T. Yamagami, R. Horisaki, E. Segawa, *Normal Variance Mixture with Arcsine Law of an Interpolating Walk Between Persistent Random Walk and Quantum Walk*, *Entropy* **27**, 670 (2025), DOI:10.3390/e27070670; arXiv:2503.03021.
4. N. Konno, *Limit theorems and absorption problems for one-dimensional correlated random walks*, *Stochastic Models* **25** (2009), 28–49, DOI:10.1080/15326340802640941; arXiv:quant-ph/0310191. Section 3 gives a Bessel-function rare-switching position-distribution limit; Section 4 treats one- and two-boundary absorption on a related but distinct persistent-walk model.
5. G. H. Weiss, *Some applications of persistent random walks and the telegrapher's equation*, *Physica A* **311** (2002), 381–410. Background on persistent-walk models; not asserted to prove the present conditional crossover.
