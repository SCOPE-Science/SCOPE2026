# Simultaneous ordered invariant graphs for the full Bernoulli rotation interval

## Finding
For every \(p\in(0,1)\), the Bernoulli circle maps specified below admit a common shift-invariant set of base sequences of probability one such that, **simultaneously for all** \(c\in[p-1,p]\), there is a measurable invariant singleton family \(K_c(\omega)=\{x_c(\omega)\}\) with
\[
f_{\omega_0}(x_c(\omega))=x_c(\sigma\omega),\qquad
\lim_{n\to\infty}\frac{F_{\omega_{n-1}}\circ\cdots\circ F_{\omega_0}(x_c(\omega))-x_c(\omega)}n=c.
\]
The restricted fibre entropy of each singleton family is zero. Moreover, \(c\mapsto x_c(\omega)\) is strictly increasing, right-continuous, and has a dense countable set of jumps with the exact sizes \(3^{-k-1}\), \(k\ge0\). The closure of its image is a Lebesgue-null Cantor set. The construction is valid for the entire interval, including both endpoints, on a single full-measure set.

## Assumptions and scope
Fix \(0<p<1\) and let \(\Omega=\{+,-\}^{\mathbb N_0}\) with Bernoulli product measure assigning \(+\) probability \(p\). Let \(\sigma\) be the one-sided shift. Write \(\mathbb T=\mathbb R/\mathbb Z\). Define the degree-one lifts on \([0,1)\) by
\[
F_+(x)=\begin{cases}3x,&0\le x<2/3,\\4-3x,&2/3\le x<1,\end{cases}
\quad F_-(x)=\begin{cases}-3x,&0\le x<1/3,\\3x-2,&1/3\le x<1,\end{cases}
\]
and extend by \(F_\pm(x+1)=F_\pm(x)+1\). Set \(f_\pm=F_\pm\bmod1\). Random compact sets here mean measurable compact-valued fibres equivariant under the displayed maps; their fibre entropy is the relative Bowen entropy of the restricted singleton dynamics. No continuity of the sections in the base is assumed.

For \(\omega=(\omega_k)_{k\ge0}\), let \(b_k(\omega)=\mathbf1_{\{\omega_k=-\}}\) and
\[
V(\omega)=\sum_{j=0}^{\infty}2^{-j-1}\mathbf1_{\{\omega_j=+\}},\quad
U(\omega)=G_p(V(\omega)),
\]
where \(G_p(t)=\mathbb P\{V\le t\}\) is the exact distribution function of the biased binary expansion. It is continuous and strictly increasing on \([0,1]\), since \(0<p<1\); hence \(U\) is uniformly distributed on \([0,1]\). Define \(t_k(\omega)=U(\sigma^{k+1}\omega)\). For \(\lambda\in[0,1]\) put
\[
x_\lambda(\omega)=\sum_{k=0}^\infty3^{-k-1}\left[b_k(\omega)+\mathbf1_{\{t_k(\omega)\le\lambda\}}\right].
\]
For the claimed rotation parameter take \(\lambda=c+(1-p)\), and \(x_c=x_\lambda\).

## Proof
**Uniform almost-sure base control.** The biased binary expansion has no atoms: every prescribed infinite digit sequence has probability at most \(\max(p,1-p)^n\) after its first \(n\) digits. Every nonempty interval contains a binary cylinder of positive probability, so its distribution function is strictly increasing and continuous. The probability integral transform makes \(U\) uniform. The ergodic theorem, applied to the stationary sequence \(t_k\), gives
\[
\frac1n\sum_{k=0}^{n-1}\mathbf1_{\{t_k\le r\}}\longrightarrow r
\]
for every rational \(r\in[0,1]\), simultaneously on a shift-invariant full-measure set. Monotone sandwiching extends the convergence to **every real** \(\lambda\in[0,1]\) on that same set. On its intersection with a further invariant full-measure set,
\[
\frac1n\sum_{k=0}^{n-1}b_k\longrightarrow1-p,
\]
the base is aperiodic, both signs recur infinitely often, all \(t_k\in(0,1)\), and the \(t_k\) are pairwise distinct. Pairwise distinctness holds because equality of two biased-binary tail encodings, apart from the zero-probability ambiguous binary expansions, would make the base eventually periodic.

**Exact invariant coding.** At step \(k\), the ternary first digit of \(x_\lambda(\sigma^k\omega)\) is \(d_k=b_k+\mathbf1_{\{t_k\le\lambda\}}\). For a plus map it belongs to \(\{0,1\}\), and for a minus map it belongs to \(\{1,2\}\). These are precisely their two increasing affine full branches. Their inverse branches are \(y\mapsto(d_k+y)/3\). Since both base signs recur infinitely often, the resulting ternary numbers never equal a branch endpoint for any \(\lambda\). Thus for all \(\lambda\), on the same full-measure set,
\[
f_{\omega_k}(x_\lambda(\sigma^k\omega))=x_\lambda(\sigma^{k+1}\omega),
\quad F_{\omega_k}(x_\lambda(\sigma^k\omega))=
 x_\lambda(\sigma^{k+1}\omega)+\mathbf1_{\{t_k\le\lambda\}}-b_k.
\]
The second identity telescopes for any \(n\). The difference of its two terminal fractional coordinates is bounded by one, and the two uniform Birkhoff limits yield the rotation \(\lambda-(1-p)=c\) for all \(\lambda\) at once. Each \(\omega\mapsto x_\lambda(\omega)\) is measurable as a uniform limit of bounded measurable sums. Hence \(K_c(\omega)=\{x_c(\omega)\}\) is a random compact equivariant singleton. Its relative Bowen separated-set size is one at every time and scale, so its fibre entropy is zero; a nonempty singleton fibre has no proper nonempty fibrewise invariant compact subfamily.

**Sharp geometry of the parameter family.** Write
\[
A_\omega=\sum_{k\ge0}3^{-k-1}b_k,\qquad
x_\lambda(\omega)=A_\omega+\nu_\omega([0,\lambda]),\qquad
\nu_\omega=\sum_{k\ge0}3^{-k-1}\delta_{t_k}.
\]
Its mass is \(1/2\). The uniform empirical distribution of \(t_k\) implies that these locations are dense, and their pairwise distinctness gives a jump of size exactly \(3^{-k-1}\) at \(t_k\). Thus \(x_\lambda\) is strictly increasing and right-continuous, with dense jumps. Its endpoint values are \(A_\omega\) and \(A_\omega+1/2\). Each jump creates a disjoint open interval \((x_{t_k-},x_{t_k})\) missing from the closure of the range. These intervals have total length \(\sum_{k\ge0}3^{-k-1}=1/2\), the complete length of the endpoint interval. The closure of the image therefore has Lebesgue measure zero and is nowhere dense. It is perfect: density of the jump locations gives strict increase, and right continuity supplies distinct range values arbitrarily close above every nonterminal range value; left limits supply the terminal endpoint and all remaining closure points. Hence it is a Cantor set. Strict order also shows different rotation labels give different invariant points.

## Verification
The included standard-library exact-rational `verify.py` checks the branch and lift identities for all \(4^n\) signed-selector words of lengths \(1\le n\le6\) (30,948 one-step identities), and the finite geometric jump-mass identity through fourteen levels. Run `python verify.py`; it prints `FINITE_IDENTITIES_OK 30948`. These checks confirm finite algebra only. The simultaneous continuum convergence and Cantor conclusion are proved above by probability, monotonicity, and infinite mass accounting, not finite tests.

## Relationship to prior work
Li, Lloyd and Romaña, arXiv:2606.16498v1, Example 3.1, obtain the full rotation interval \([p-1,p]\) and explicitly exhibit endpoint orbits, and their Example 4.1 computes entropy \(\log3\). Their Section 5, Question 1 asks whether each rotation value can be realized on a compact equivariant random set, possibly with zero entropy. The present theorem affirmatively settles that question for their explicit Bernoulli model **only**, simultaneously in the rotation parameter, and adds exact dense-jump/null-Cantor geometry of the ordered family. It does not prove Question 1 in the authors' general ergodic-base setting.

Glendinning, Jäger and Stark (2008/2009) establish minimal-set realization for **continuous uniquely ergodically forced** circle maps, under a different forcing hypothesis. The present Bernoulli measurable forcing is not covered by that statement. Full-branch coding and the ergodic theorem are standard tools; the explicit simultaneous selector and its sharp section geometry are the claimed specialization.

## Limitations
The theorem applies only to the specified full-branch Bernoulli family with \(0<p<1\). It neither establishes invariant-graph realization for arbitrary random degree-one circle maps nor guarantees continuous dependence on \(c\); indeed the exhibited dependence is discontinuous at a dense countable set. The null Cantor statement concerns the **closure of the parameter-section range for each typical base**, not the dimension of the full skew-product invariant set. The construction uses measurable future-dependent choices and not extra independent randomness. No independent mathematical audit is claimed.

## References
1. Zixu Li, Simon Lloyd, Sergio Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1 (15 June 2026), Sections 3.6, 4, and 5. https://arxiv.org/abs/2606.16498
2. P. A. Glendinning, T. Jäger, J. Stark, *Strangely Dispersed Minimal Sets in the Quasiperiodically Forced Arnold Circle Map*, arXiv:0807.4707 (2008); *Nonlinearity* 22 (2009), 835–854. https://arxiv.org/abs/0807.4707
