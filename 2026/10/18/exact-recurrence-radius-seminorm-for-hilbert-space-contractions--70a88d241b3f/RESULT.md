# Exact recurrence-radius seminorm for Hilbert-space contractions

## Finding

Let \(T\) be any contraction on a complex Hilbert space \(H\), and let \(P\) denote the orthogonal projection onto the closed span of all eigenvectors of \(T\) with eigenvalue on the unit circle. The strong limit
\[
A=\operatorname*{s\!\!\!-\!lim}_{n\to\infty}T^{*n}T^n
\]
exists and is a positive contraction. For \(x\in H\), write \(y=Px\) and \(z=(I-P)x\). The **exact threshold for syndetic approximate returns to the initial point** is
\[
\boxed{\ x\in AP_\delta(T)\ \Longleftrightarrow\
\delta^2\ge\|z\|^2+\langle Az,z\rangle\ }
\qquad (x\in H,\ \delta\ge0).
\]
In particular, the recurrence radius of every vector is the continuous Hilbertian seminorm
\[
\boxed{\ \delta_*(x)=\left(\|(I-P)x\|^2+\|A^{1/2}(I-P)x\|^2\right)^{1/2}.\ }
\]
Its nullspace is exactly the almost-periodic pure-point unitary subspace \(PH\), its Lipschitz constant is at most \(\sqrt2\), and every \(AP_\delta(T)\) is a closed, convex, possibly unbounded ellipsoidal cylinder over \(PH\).

## Assumptions and scope

A **contraction** means a bounded linear operator \(T:H\to H\) with \(\|T\|\le1\); no normality, separability, injectivity, or stability assumption is made. Positive time \(n\) ranges over \(\mathbb N=\{1,2,\ldots\}\). A subset \(E\subset\mathbb N\) is **syndetic** if there is an integer \(L\ge1\) for which every interval of \(L\) consecutive positive integers contains an element of \(E\).

For \(\delta\ge0\), the **base-point** class \(AP_\delta(T)\) is defined by the quantifiers
\[
 x\in AP_\delta(T)\quad\Longleftrightarrow\quad
 (\forall\epsilon>0)(\exists L\ge1)(\forall m\ge1)
 (\exists n\in\{m,\ldots,m+L-1\})\ 
 \|T^n x-x\|<\delta+\epsilon.
\]
Its radius is \(\delta_*(x)=\inf\{\delta\ge0:x\in AP_\delta(T)\}\). This is **not** the stronger notion requiring \(\sup_{k\ge0}\|T^{n+k}x-T^k x\|\) to be small. The defining power limit \(A\) exists because the positive operators \(T^{*n}T^n\) form a decreasing, bounded family; for each \(z\), \(\langle Az,z\rangle=\lim_{n\to\infty}\|T^n z\|^2\).

## Proof

**1. Reducing almost-periodic sector.** Let \(Tv=\lambda v\), where \(|\lambda|=1\). Since \(\|Tv\|=\|v\|\) and \(I-T^*T\) is positive, \((I-T^*T)v=0\); therefore \(T^*v=\bar\lambda v\). Hence each such eigenspace reduces \(T\), and eigenspaces belonging to distinct unimodular eigenvalues are orthogonal. Consequently \(P\) is an orthogonal reducing projection. The restriction \(T|_{PH}\) is a pure-point unitary. For every \(y\in PH\) and every \(\eta>0\), the set
\[
 E_\eta(y)=\{n\ge1:\|T^n y-y\|<\eta\}
\]
is syndetic. Indeed, approximate \(y\) in norm by a finite sum of unimodular eigenvectors. Their orbit lies in a finite-dimensional compact torus, and return times to each neighborhood of the identity under a torus rotation are syndetic: finite translates of any nonempty open neighborhood cover the compact orbit closure. The approximation error is uniformly controlled because \(T\) is contractive.

**2. A uniform spectral decorrelation lemma.** Fix \(z\in (I-P)H\), and put \(\phi(n)=\langle T^n z,z\rangle\). By the unitary dilation theorem for contractions, there is a finite positive Borel measure \(\nu\) on the unit circle \(\mathbb T\) such that
\[
 \phi(n)=\int_{\mathbb T}\zeta^n\,d\nu(\zeta),\qquad n\ge0.
\]
This measure has no atoms. To see this, fix \(\lambda\in\mathbb T\). By dominated Cesàro averaging in the preceding integral,
\[
 \nu(\{\lambda\})=
 \lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}\bar\lambda^{\,n}\phi(n).
\]
The Hilbert-space mean ergodic theorem for the contraction \(\bar\lambda T\) identifies the right side with \(\langle P_\lambda z,z\rangle\), where \(P_\lambda\) projects onto \(\ker(T-\lambda I)\). Since \(P_\lambda z=0\), this atom is zero. The assertion holds also for nonseparable \(H\), because the scalar measure is finite.

An elementary uniform version of Wiener's squared-Fourier-coefficient lemma now gives
\[
 \lim_{N\to\infty}\sup_{m\ge0}\frac1N
 \sum_{n=m}^{m+N-1}|\phi(n)|^2=0.
 \tag{1}
\]
Indeed, writing the square as a double integral and summing a geometric progression yields, uniformly in \(m\),
\[
 \left|\frac1N\sum_{n=m}^{m+N-1}|\phi(n)|^2\right|
 \le\iint_{\mathbb T^2}
 \min\left\{1,\frac2{N|1-\zeta\bar\xi|}\right\}
 \,d\nu(\zeta)\,d\nu(\xi).
\]
The diagonal \(\{\zeta=\xi\}\) has zero \(\nu\otimes\nu\)-measure because \(\nu\) is nonatomic. Dominated convergence proves (1). In particular, for each \(c>0\) the set \(\{n:|\phi(n)|\ge c\}\) has upper Banach density zero, in the explicit uniform-block sense: its proportion in every block of length \(N\) tends uniformly to zero as \(N\to\infty\).

**3. Exact threshold from competing return sets.** Write \(x=y+z\) with \(y=Px\) and \(z=(I-P)x\). Reducing orthogonality gives, for every integer \(n\ge0\),
\[
 \|T^n x-x\|^2=\|T^n y-y\|^2+\|z\|^2
 +q_n-2\operatorname{Re}\phi(n),
 \qquad q_n=\|T^n z\|^2.
 \tag{2}
\]
The sequence \(q_n\) decreases to \(q=\langle Az,z\rangle\). Set \(d=\sqrt{\|z\|^2+q}\).

*Necessity:* Suppose \(0\le\delta<d\). Choose \(\epsilon>0\) with \(\delta+\epsilon<d\), and put \(c=(d^2-(\delta+\epsilon)^2)/2>0\). Since \(q_n\ge q\) and the first term on the right of (2) is nonnegative, every return with \(\|T^n x-x\|<\delta+\epsilon\) forces \(\operatorname{Re}\phi(n)>c\). Were these returns syndetic, the set \(\{n:|\phi(n)|>c\}\) would have positive lower density in all long blocks, contradicting (1). Thus \(x\notin AP_\delta(T)\).

*Sufficiency:* Fix \(\epsilon>0\), and choose \(\eta>0\) so small that \(d^2+\eta^2+3\eta<(d+\epsilon)^2\). The set \(E_\eta(y)\) from step 1 is syndetic; let \(L_0\) be a bound on its gaps. Equation (1) and the Markov bound imply that for all sufficiently long blocks, uniformly over the block's location, the number of \(n\) with \(|\phi(n)|\ge\eta\) is smaller than half the number of points guaranteed in that block by the gap bound \(L_0\). Therefore the set of common times
\[
 F=E_\eta(y)\cap\{n\ge1:|\phi(n)|<\eta\}
\]
is itself syndetic. (Explicitly, choose a block length large enough to force at least \(\lfloor N/L_0\rfloor\) members of \(E_\eta(y)\), and fewer than this number of exceptional indices; the same argument applies at every block location.) For all sufficiently large \(n\), \(q_n<q+\eta\). At all such times in \(F\), equation (2) yields
\[
 \|T^n x-x\|^2<\eta^2+\|z\|^2+(q+\eta)+2\eta
 =d^2+\eta^2+3\eta<(d+\epsilon)^2.
\]
Deleting finitely many indices from a syndetic set preserves syndeticity (after enlarging its gap bound). Hence for every \(\epsilon>0\) the \((d+\epsilon)\)-return set is syndetic, so \(x\in AP_d(T)\). Monotonicity gives the same result for every \(\delta\ge d\), completing the equivalence.

**4. Geometry.** Since \(A\ge0\),
\[
 \delta_*(x)=\left\|\bigl((I-P)x,A^{1/2}(I-P)x\bigr)\right\|_{H\oplus H}.
\]
It is therefore a seminorm with nullspace exactly \(PH\), and
\[|\delta_*(x)-\delta_*(x')|\le\sqrt2\|x-x'\|.\]
Its sublevel sets have the stated cylinder geometry.

## Verification

The proof has no finite-dimensional truncation or enumeration step: each universal quantifier is discharged by the unitary dilation, mean ergodic theorem, a uniform Fourier averaging estimate, and an intersection argument for syndetic and uniformly sparse sets. The optional standalone script `check_examples.py` uses only the Python standard library and checks exact rational identities in sample operators. These examples are diagnostics and **are not** an infinite-dimensional proof.

Consequences can be checked directly:

- For a strongly stable contraction, \(A=0\) and there are no nonzero unimodular eigenvectors; hence \(\delta_*(x)=\|x\|\), recovering the known stable-orbit threshold.
- For an isometry, \(A=I\), so \(\delta_*(x)=\sqrt2\|(I-P)x\|\). A unilateral forward shift has \(P=0\), whereas a unilateral backward shift is strongly stable and has \(A=0\).
- A forward weighted shift with weights \(w_0=1/2\) and \(w_k=1\) for \(k\ge1\) satisfies \(P=0\) and \(\delta_*(e_0)=\sqrt5/2\); this lies strictly between the backward-shift and isometric-shift thresholds.
- For a normal contraction, its spectral measure splits into an atomic unit-circle part, a continuous unit-circle part, and an open-unit-disk part. The squared radius carries coefficients \(0\), \(2\), and \(1\), respectively.

## Relationship to prior work

Alshammari and Benchiheb, *δ-Almost Periodic Vectors for Bounded Linear Operators: Geometric and Dynamical Structure* (2026), introduced the exact base-point recurrence definition and the recurrence radius. Its Theorem 2.2 gives the radius for strongly stable orbits, and its Proposition 3.5 proves lower semicontinuity under power-boundedness. The inspected sections on geometry and weighted shifts do not provide an exact formula for arbitrary Hilbert-space contractions, including those with persistent continuous-spectrum components. The present formula is a quantitative global classification, not a rephrasing of the stable-orbit case.

Alshammari, *Return-Time Profiles and Quantitative Recurrence for Uniformly δ-Almost Periodic Vectors* (2026), explicitly uses the stronger whole-orbit translation supremum. Its profile does not directly evaluate the base-point radius studied here. The key proof ingredients—unitary dilation, the mean ergodic theorem, and Wiener's Fourier averaging lemma—are classical. The claimed contribution is their combination into an exact recurrence-radius formula and a Hilbertian seminorm classification for all contractions, not the auxiliary spectral theorems themselves.

## Limitations

The theorem requires Hilbert geometry and contractivity; it does not assert the formula for all power-bounded operators on arbitrary Banach spaces, nor characterize the stronger orbit-translation return-time profile. The recurrence threshold gives existence of bounded-gap approximate returns but does not produce an optimal numerical bound on their gaps as the tolerance tends to the critical value. Publication-priority risk remains from classical spectral-recurrence literature that may formulate an equivalent invariant; the mathematical argument is self-contained modulo explicitly stated classical theorems. No independent external audit is claimed.

## References

1. H. O. Alshammari and O. Benchiheb, “δ-Almost Periodic Vectors for Bounded Linear Operators: Geometric and Dynamical Structure,” *Journal of Function Spaces* (first published 12 May 2026), doi:10.1155/jofs/9920770, https://doi.org/10.1155/jofs/9920770.
2. H. O. Alshammari, “Return-Time Profiles and Quantitative Recurrence for Uniformly δ-Almost Periodic Vectors,” *Mathematics* **14** (2026), 1986 (published 4 June 2026), doi:10.3390/math14111986, https://doi.org/10.3390/math14111986.
3. Classical Sz.-Nagy unitary dilation theorem, von Neumann mean ergodic theorem, and Wiener's lemma on squared Fourier coefficients of finite measures; their precise forms needed here are given and applied in the proof.
