# Positive-density overshoots and curvature reversals of finite-support renewal masses

## Finding
For every nondegenerate, finitely supported, aperiodic positive-integer interarrival law, the renewal probabilities approach their renewal-theorem limit from both sides on sets of **positive lower natural density**. The discrete curvature also has each strict sign on sets of positive lower natural density. In particular, neither the renewal masses nor their eventual positive successive ratios can be eventually monotone; no finite tail can be entirely log-convex or entirely log-concave.

More precisely, let \(u_n=\Pr\{n=S_k\text{ for some }k\ge0\}\), \(\mu=\mathbb E[X_1]\), and \(L=1/\mu\). Define \(e_n=u_n-L\) and \(h_n=u_{n-1}u_{n+1}-u_n^2\) for \(n\ge1\). Each of the four sets \(\{n:e_n>0\}\), \(\{n:e_n<0\}\), \(\{n:h_n>0\}\), and \(\{n:h_n<0\}\) has positive lower natural density. All assertions hold even when \(\Pr(X_1=1)=0\), provided the support gcd is one.

## Assumptions and scope
The random variables \(X_1,X_2,\ldots\) are independent and identically distributed, take values in a finite subset \(S\subset\{1,2,\ldots\}\) with \(|S|\ge2\), and have positive probabilities \(p_j>0\) exactly on \(S\). Assume \(\gcd(S)=1\). Set \(S_0=0\) and \(S_k=\sum_{i=1}^k X_i\). Because increments are positive, the events \(S_k=n\) are disjoint in \(k\), so the definition of \(u_n\) is equivalent to \(u_n=\sum_{k\ge0}\Pr(S_k=n)\). The lower density of \(A\subseteq\mathbb N\) is \(\underline d(A)=\liminf_{N\to\infty}N^{-1}|A\cap\{1,\ldots,N\}|\).

The law is neither deterministic nor periodic. Deterministic unit increments have constant renewal mass and are excluded; an infinite-support geometric distribution can also have an eventually constant renewal mass, so finite support is essential to the stated universal class. No numerical claim about the earliest sign change or uniform lower bound over all laws is made.

## Proof
**1. Renewal rational function and pole geometry.** Let \(f(z)=\sum_{j\in S}p_jz^j\) and \(U(z)=\sum_{n\ge0}u_nz^n=1/(1-f(z))\), valid initially for \(|z|<1\). Since \(f(1)=1\) and \(f'(1)=\mu>0\), \(U\) has a simple pole at \(1\) with principal part \(L/(1-z)\). For \(|z|\le1\), the bound \(|f(z)|\le f(|z|)\le1\) rules out roots of \(1-f\) in the open disk. Equality on the unit circle forces \(z^j=1\) for every \(j\in S\), hence \(z=1\) by the gcd assumption. On the positive real axis, \(f'(x)>0\), so \(f(x)=1\) holds only at \(x=1\). Since \(f\) has degree at least two, \(1-f\) has roots besides \(1\); all are of modulus greater than one, none lies on the positive real axis.

Thus \(H(z)=U(z)-L/(1-z)\) is rational and its finite poles are precisely those other roots, with their multiplicities. In particular, \(e_n=[z^n]H(z)\) decays exponentially.

**2. Dominant poles and positive frequencies of either sign.** Let \(R>1\) be the least modulus among the poles of \(H\), let \(m\ge1\) be the greatest multiplicity among poles on \(|z|=R\), and let \(J\) index the poles \(z_j=R e^{i\theta_j}\) of multiplicity \(m\). Partial fractions give nonzero complex coefficients \(c_j\) such that
\[
 e_n=R^{-n}n^{m-1}\bigl(v_n+o(1)\bigr),\qquad v_n=\sum_{j\in J}c_je^{-in\theta_j}.
\]
The error tends to zero uniformly as the integer \(n\) grows. The set of dominant poles is closed under conjugation, so \(v_n\) is real. None of the \(\theta_j\) vanishes modulo \(2\pi\), since \(H\) has no positive real pole; the angles are distinct. Finite geometric sums therefore give
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N v_n=0,\qquad
\lim_{N\to\infty}\frac1N\sum_{n=1}^N v_n^2=A:=\sum_{j\in J}|c_j|^2>0.
\]
Also \(|v_n|\le B:=\sum_{j\in J}|c_j|\). For any bounded real sequence \(t_n\) with Cesàro mean zero, mean square \(A>0\), and \(|t_n|\le B\), the inequalities \(|t_n|\ge t_n^2/B\) and \(t_n^+=(|t_n|+t_n)/2\) yield \(\liminf_N N^{-1}\sum_{n\le N}t_n^+\ge A/(2B)\), and likewise for \(t_n^-\). Taking \(\delta=A/(4B)\) and bounding \(t_n^+\le\delta+B\mathbf1_{\{t_n>\delta\}}\) shows
\[
 \underline d\{n:t_n>\delta\}\ge A/(4B^2)>0,
 \quad \underline d\{n:t_n<-\delta\}\ge A/(4B^2)>0.
\]
Apply this with \(t_n=v_n\). The \(o(1)\) error eventually has magnitude less than \(\delta\), so both strict signs of \(e_n\) have lower densities at least \(A/(4B^2)\).

**3. Curvature inherits nonvanishing mean-zero frequencies.** As \(n\to\infty\),
\[
 h_n=L(e_{n-1}+e_{n+1}-2e_n)+(e_{n-1}e_{n+1}-e_n^2).
\]
Since \(e_n\) decays exponentially, the second parenthesis is of lower order. Consequently
\[
 h_n=LR^{-n}n^{m-1}\bigl(w_n+o(1)\bigr),\quad
 w_n=\sum_{j\in J}c_j(z_j+z_j^{-1}-2)e^{-in\theta_j}.
\]
Here \(z_j+z_j^{-1}-2=(z_j-1)^2/z_j\ne0\), so every displayed frequency has nonzero coefficient. Again \(w_n\) is real, has Cesàro mean zero and strictly positive mean square \(\sum_j|c_j(z_j+z_j^{-1}-2)|^2\). The density lemma from step 2 proves both strict curvature signs on sets of positive lower density.

**4. Consequences for eventual monotonicity and ratios.** The numerical semigroup generated by finite \(S\) of gcd one contains every sufficiently large integer, so \(u_n>0\) eventually. From the exponential convergence above, \(u_n\to L>0\), and consequently \(u_{n+1}/u_n\to1\). The sign alternations of \(e_n\) rule out an eventually monotone \(u_n\). If eventual ratios were nondecreasing, their limit one would force each sufficiently late ratio to be at most one and hence \(u_n\) eventually nonincreasing, a contradiction; if nonincreasing, the same reasoning forces eventually nondecreasing masses. Finally, the sign of the successive-ratio difference equals the sign of \(h_n\) for sufficiently large \(n\) (because all renewal masses in its denominator are positive). The positive-density conclusion for \(h_n\) is therefore strictly stronger than just infinitely many rises and falls.

## Verification
The accompanying `verify_renewal.py` computes the renewal recurrence in exact rational arithmetic for four nondegenerate aperiodic finite-support laws, including two laws with \(p_1=0\). It checks each sign in the finite window \(60\le n\le180\) for the renewal-limit error and curvature. The companion `verification_output.txt` records the executed result. These finite checks are illustrative only; the proof for every support and probability vector is the pole/Cesàro argument above. As a separate transparent check, for \(p_1=p_2=1/2\) one obtains exactly \(u_n=2/3+(1/3)(-1/2)^n\) and \(h_n=-(-1/2)^n\), making the two kinds of alternation explicit.

## Relationship to prior work
The finite-support discrete renewal recursion and limiting renewal rate are classical, as presented in Lalley's notes. Berenhaut and Lund (2001) investigate geometric convergence rates from hazard conditions and bounds for finite-support laws; convergence-rate bounds alone do not imply any positive density of errors of either sign, and the full text could not be inspected. Yu (2010) studies how concavity of renewal functions relates to interarrival aging properties, a different geometric/shape question. Nikolov and Savov (2023, Proposition 3.1, full text inspected) establish that renewal masses are not ultimately monotone when \(0<p_1<1\), and sandwich them between monotone envelope sequences. Their qualitative statement already implies that successive ratios cannot be eventually monotone in that parameter range, so the purely qualitative ratio corollary here is not claimed as a novel result. The present finding instead gives **positive lower-density overshoots and undershoots of the renewal limit, positive lower-density signs of local curvature, and support-gcd-one generality including \(p_1=0\)**. Neither the cited eventual-nonmonotonicity proposition nor a geometric convergence-rate bound, as stated, implies these density conclusions.

## Limitations
The result is restricted to nondegenerate finite-support aperiodic laws, and it does not establish exact natural densities, optimal uniform density constants, sign-change spacings, or robustness to unbounded support. The source search did not prove worldwide historical novelty. Full texts of the Berenhaut–Lund convergence-rate article and Liggett's total-positivity chapter could not be inspected; their full contents might contain stronger equivalent results. The evidence establishes the stated theorem mathematically, not independent validation or historical priority.

## References
- Y. Yu (2010), *Concave Renewal Functions Do Not Imply DFR Inter-Renewal Times*, first public preprint 2010-09-13, arXiv:1009.2463v1, https://arxiv.org/abs/1009.2463.
- N. Nikolov and M. Savov (2023), *Properties and conjectures regarding discrete renewal sequences*, arXiv:2307.00545v1, https://arxiv.org/abs/2307.00545; especially Proposition 3.1.
- K. S. Berenhaut and R. Lund (2001), *Geometric renewal convergence rates from hazard rates*, Journal of Applied Probability 38, 180–194, https://doi.org/10.1239/jap/996986652.
- S. P. Lalley, *Renewal Theory* (lecture notes), https://galton.uchicago.edu/~lalley/Courses/383/Renewal.pdf.
- T. M. Liggett (1989), *Total positivity and renewal theory*, in *Probability, Statistics, and Mathematics*, pp. 141–162 (bibliographic comparison only; full text not available).
