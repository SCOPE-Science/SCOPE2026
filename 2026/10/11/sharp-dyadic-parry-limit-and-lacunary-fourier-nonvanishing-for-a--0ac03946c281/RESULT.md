# Sharp dyadic Parry limit and lacunary Fourier nonvanishing for a golden-mean measure

## Finding
Let \(\varphi=(1+\sqrt5)/2\), \(p=\varphi^{-1}\), and \(q=\varphi^{-2}=1-p\). Consider the unique Borel probability measure \(\mu\) defined by
\[
\mu=p(S_0)_\#\mu+q(S_1)_\#\mu,\qquad
S_0(x)=\frac x2,\quad S_1(x)=\frac x4+\frac12.
\]
On the circle \(\mathbb T=\mathbb R/\mathbb Z\), put \(T(x)=2x\pmod1\), \(\mu_n=(T^n)_\#\mu\), and
\[
\nu=\frac{\mu+q(S_0)_\#\mu}{1+q}.
\]
Then \(\nu\) is the stationary Parry measure of the binary golden-mean shift, pushed forward by binary expansion. More precisely, for every integer \(n\ge0\),
\[
\boxed{\mu_n=\nu+(-q)^n(\mu-\nu),\qquad
 d_{\mathrm{TV}}(\mu_n,\nu)=\frac{q^{n+2}}{1+q}.}
\]
Here \(d_{\mathrm{TV}}(\eta,\xi)=\sup_{E\ \mathrm{Borel}}|\eta(E)-\xi(E)|\) for probability measures. The displayed distance is an *equality*, not just an upper bound; thus its exponential rate is sharp.

For the positive-frequency Fourier convention \(F(t)=\int e^{2\pi itx}\,d\mu(x)\), the same theorem includes the infinite arithmetic nonvanishing result
\[
\boxed{\operatorname{Im}F(2^n)>\frac15\quad\text{for every integer }n\ge0.}
\]
Hence \(F\) has no zero on \(\{2^n:n\ge0\}\) or its negative. In particular it does not decay at infinity, although nondecay itself was known previously.

## Assumptions and scope
All measures are Borel probabilities. The support of \(\mu\) lies in \([0,2/3]\), and the images \(S_0([0,2/3])=[0,1/3]\) and \(S_1([0,2/3])=[1/2,2/3]\) are disjoint. We use the *positive* Fourier exponential; changing convention conjugates the coefficient and reverses the sign of its imaginary part, without affecting nonvanishing. The bounds cover all nonnegative integers \(n\) and no real continuum beyond the stated frequencies.

## Proof
**1. Renewal words and the Parry identification.** The binary expansion of \(S_0(x)\) prepends the one-digit word \(0\), while that of \(S_1(x)\) prepends \(10\). Consequently \(\mu\) is the binary image of independent concatenations of words \(0\) and \(10\), selected with probabilities \(p\) and \(q\). Every zero ends a word. The successive binary digits therefore form a Markov chain with initial distribution \((p,q)\) and transition matrix, in digit order \((0,1)\),
\[
P=\begin{pmatrix}p&q\\1&0\end{pmatrix}.
\]
Its stationary distribution is \(\pi=(1/(1+q),q/(1+q))\), and the second eigenvalue is \(-q\). For the golden-mean adjacency matrix \(A=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), a positive Perron vector is \((\varphi,1)\), with Perron root \(\varphi\); the associated Parry transition probabilities are exactly \(P\). Thus its stationary binary measure is the maximal-entropy Parry measure. Its entropy per binary digit is
\[
\frac{-p\log p-q\log q}{1+q}=-\log p=\log\varphi.
\]
Binary-coding ambiguities occur only at dyadic rationals; the measures here are atomless, since the largest mass of a length-\(r\) independent-word cylinder is at most \(\max(p,q)^r\to0\).

**2. Exact measure recurrence.** The identities on \(\mathbb T\),
\[
T\circ S_0=\mathrm{id},\qquad T\circ S_1=S_0,
\]
give \(\mu_1=p\mu+q(S_0)_\#\mu\). Moreover, for every \(n\ge2\),
\[
T^n\circ S_0=T^{n-1},\qquad T^n\circ S_1=T^{n-2}
\]
(the translation in the second map becomes an integer). Applying the self-similar identity yields
\[
\mu_n=p\mu_{n-1}+q\mu_{n-2} \quad(n\ge2).
\]
Since \(p+q=1\), its two characteristic roots are \(1\) and \(-q\), and
\[
\nu=\frac{\mu_1+q\mu_0}{1+q}
=\frac{\mu+q(S_0)_\#\mu}{1+q}
\]
is the stationary component. Solving the *measure-valued* recurrence gives \(\mu_n=\nu+(-q)^n(\mu-\nu)\) for all \(n\ge0\). It follows also that \(T_\#\nu=\nu\). Uniqueness of the stationary Parry law identifies this invariant limit with the law in Step 1.

**3. Equality in total variation.** By the defining self-similarity,
\[
\mu-\nu
=\frac{q}{1+q}\bigl(\mu-(S_0)_\#\mu\bigr)
=\frac{q^2}{1+q}\bigl((S_1)_\#\mu-(S_0)_\#\mu\bigr).
\]
The two measures inside the final parentheses are mutually singular because their supports are separated. Their difference has probability total-variation norm exactly \(1\) (and signed-measure variation norm exactly \(2\)). Multiplication by \((-q)^n\) proves the asserted exact distance \(q^{n+2}/(1+q)\), including the endpoints \(n=0,1\). As this is positive for every \(n\), the exponent cannot be improved.

**4. Certified infinite Fourier nonvanishing.** The transform satisfies
\[
F(t)=pF(t/2)+q e^{\pi i t}F(t/4).
\]
Let \(u_n=\operatorname{Im}F(2^n)\). For every integer \(n\ge2\), the exponential phase equals \(1\); hence
\[
u_n=p u_{n-1}+q u_{n-2}.
\]
A standalone outward interval-arithmetic computation, with an explicitly bounded analytic truncation remainder, certifies
\[
0.224<\operatorname{Im}F(1)<0.226,\qquad
0.384<\operatorname{Im}F(2)<0.386.
\]
Since \(p,q>0\) and \(p+q=1\), induction yields \(u_n>1/5\) for every \(n\ge0\). This is not an inference from a finite grid; the grid-independent recurrence supplies the infinite step.

## Verification
The provided `verify_golden_dyadic.py` uses 45-decimal-digit outward interval arithmetic to compute the two base Fourier coefficients via the functional equation at a fixed recursion depth of \(36\). The exact support bound implies
\[
|F(t/2^{36})-1|\le\frac{4\pi|t|}{3\cdot2^{36}},
\]
and the same or a smaller error at the following terminal level. Each backward recurrence has nonnegative weights summing to one and a unimodular phase; its error is therefore no larger than this terminal bound. Using the rational inequality \(\pi<22/7\) makes the error allowance independent of numerical approximations to \(\pi\). The script checks outward enclosures strictly inside the displayed rational intervals. All remaining conclusions are exact algebraic measure identities, not extrapolations from tests.

## Relationship to prior work
Mao and Wu introduced and studied this measure's spectrality and Fourier zero question; they already prove nondecay and report extensive numerical zero searches. We claim **neither general nondecay nor the full zero-free conjecture** as new. A published 2026 computer-assisted result certifies an interval \([-1000,1000]\) free of Fourier zeros, which handles finitely many dyadic powers but cannot by itself establish the entire infinite set. The new claim is the specific maximal-entropy stationary identification, **exact strong total-variation law**, and rigorously uniform positive sine bound on *all* dyadic powers. Brémont's 2021 general Pisot-form theory proves weak limiting distribution under dilation; its inspected Theorems 2.5–2.7 do not supply this measure-specific exact total-variation formula or the stated lacunary phase inequality. The generic Parry transition formula itself is classical and is not claimed as new.

## Limitations
The result does **not** settle whether \(F(t)\ne0\) at arbitrary non-dyadic real frequencies, nor whether \(\mu\) is spectral. The source's complete 2026 manuscript could not be inspected; a hidden overlapping argument is the principal residual originality risk. The sine certificate depends on interval arithmetic plus the explicit analytic tail estimate; ordinary floating-point sampling would not establish the strict inequalities. The entropy identity and Markov mixing mechanism are classical; novelty is restricted to the concrete golden-mean measure, its sharp total-variation identity, and its infinite Fourier nonvanishing certificate. Independent external review has not been performed.

## References
1. Yi-Qiu Mao and Zhi-Yi Wu, *On the spectrality of the non-homogeneous golden-mean self-similar measure*, arXiv:2609.04701 (first public September 4, 2026).
2. Julien Brémont, *Self-similar measures and the Rajchman property*, Annales Henri Lebesgue 4 (2021), 973–1004, doi:10.5802/ahl.94, especially Theorems 2.5–2.7.
3. *A certified zero-free interval [-1000,1000] for the golden-mean self-similar Fourier transform*, published mathematical finding (October 4, 2026).\n4. Classical Perron–Frobenius/Parry measure description of the golden-mean subshift with adjacency matrix \(\begin{pmatrix}1&1\\1&0\end{pmatrix}\).
