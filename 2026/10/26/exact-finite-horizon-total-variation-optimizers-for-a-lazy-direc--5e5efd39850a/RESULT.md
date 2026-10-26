# Exact finite-horizon total-variation optimizers for a lazy directed triangle

## Finding

**Theorem (complete finite-horizon optimum).** Let \(S\) be clockwise rotation on the three states \(\mathbb Z/3\mathbb Z\), let \(P_p=(1-p)I+pS\), and let \(U\) be their uniform law. For every integer \(h\ge 2\), write
\[
d_h(p)=\max_{i\in\mathbb Z/3\mathbb Z}\left\|P_p^h(i,\cdot)-U\right\|_{\mathrm{TV}},\qquad 0\le p\le1.
\]
Exactly two choices of \(p\) minimize this distance:
\[
\boxed{p_h^{\pm}=\frac12\pm\frac{1}{2\sqrt3}\tan\frac{\pi}{6h}.}
\]
Their common exact optimum is
\[
\boxed{\min_{0\le p\le1}d_h(p)=\frac{\sqrt3}{3\,2^h}\sec^h\!\left(\frac{\pi}{6h}\right).}
\]
In contrast, the nontrivial eigenvalue modulus \(\rho(p)=\sqrt{1-3p(1-p)}\) is uniquely minimized at \(p=1/2\). That choice never minimizes finite-horizon total variation for \(h\ge2\), because
\[
\frac{\min_p d_h(p)}{d_h(1/2)}
=\frac{\sqrt3}{2}\sec^h\!\left(\frac{\pi}{6h}\right)<1,
\qquad \lim_{h\to\infty}\frac{\min_p d_h(p)}{d_h(1/2)}=\frac{\sqrt3}{2}.
\]
Moreover,
\[
p_h^{\pm}=\frac12\pm\frac{\pi}{12\sqrt3\,h}+O(h^{-3}),
\quad
\frac{\min_p d_h(p)}{d_h(1/2)}
=\frac{\sqrt3}{2}\left(1+\frac{\pi^2}{72h}+O(h^{-2})\right).
\]
At the exceptional horizon \(h=1\), the complete minimizing set is \([1/3,2/3]\), and its minimum is \(1/3\).

## Assumptions and scope

The states are ordered cyclically. At each step a particle stays put with probability \(1-p\) and otherwise moves clockwise with probability \(p\), independently of preceding coin flips. The parameter includes the endpoints \(p=0,1\), which are not ergodic but still have stationary uniform law. The objective is the **exact** worst-initial-state total-variation distance after a fixed positive integer horizon. It is not the asymptotic exponential rate nor the minimum number of steps needed to cross a specified tolerance. Translation invariance makes the distance the same for all three deterministic initial states. Equivalently, it is the distance of \(\mathrm{Binomial}(h,p)\bmod3\) from uniform.

## Proof

Set \(\omega=e^{2\pi i/3}\), \(z=1-p+p\omega\), and write \(z=r e^{i\theta}\) with \(\theta\in[0,2\pi/3]\). Fourier inversion on the three-element cyclic group gives, for each residue \(k\),
\[
P_p^h(0,k)-\frac13
=\frac{2r^h}{3}\cos\left(h\theta-\frac{2\pi k}{3}\right).
\]
For any three real numbers whose sum is zero, one half their sum of absolute values equals their largest absolute value. Consequently, with
\[
H(t)=\max_{k=0,1,2}\left|\cos\left(t-\frac{2\pi k}{3}\right)\right|,
\]
we have the exact identity \(d_h(p)=\frac23r^h H(h\theta)\). Trigonometric geometry gives
\[
H(t)=\cos\!\left(\operatorname{dist}\left(t,\frac\pi3\mathbb Z\right)\right),
\quad\frac{\sqrt3}{2}\le H(t)\le1,
\]
where distance to the nearest grid point lies in \([0,\pi/6]\).

Put \(x=\theta-\pi/3\). Because \(z\) traverses the straight segment between \(1\) and \(\omega\), elementary right-triangle geometry (or solving for real and imaginary parts) gives
\[
-\frac\pi3\le x\le\frac\pi3,
\qquad r=\frac1{2\cos x},
\qquad p=\frac12+\frac{\tan x}{2\sqrt3}.
\]
The function \(H\) has period \(\pi/3\), so \(H(h\theta)=H(hx)\) for integer \(h\). Thus
\[
d_h(p)=\frac{2}{3\,2^h}\frac{H(hx)}{\cos^h x}.
\]
This expression is even in \(x\). Fix \(h\ge2\), and let \(a=\pi/(6h)\). If \(a\le|x|\le\pi/3\), then \(H(hx)\ge\sqrt3/2\) while \(\cos|x|\le\cos a\). Therefore \(d_h(p)\ge\sqrt3/(3\,2^h\cos^h a)\), with strict inequality for \(|x|>a\). At \(|x|=a\), equality holds because \(H(ha)=H(\pi/6)=\sqrt3/2\).

For \(0\le |x|<a\), the nearest multiple of \(\pi/3\) to \(h|x|\) is zero, so \(H(hx)=\cos(h|x|)\). On \((0,a)\), the logarithmic derivative of its quotient by \(\cos^h x\) equals
\[
h\{\tan x-\tan(hx)\}<0,
\]
because \(h\ge2\) and \(0<x<hx<\pi/6\). Hence the value decreases strictly down to \(|x|=a\). These two regions prove that precisely \(x=\pm a\) minimize \(d_h\), yielding the two stated choices of \(p\) and the exact minimum.

At \(p=1/2\) one has \(x=0\), hence \(d_h(1/2)=2/(3\,2^h)\). Strict concavity of \(\log\cos t\) on \([0,\pi/6]\), together with its value zero at the origin, implies for \(h\ge2\) that \(h\log\cos(\pi/(6h))>\log\cos(\pi/6)\). This proves the displayed strict ratio. The spectral statement follows immediately from \(|z|^2=1-3p(1-p)\), and the expansions follow by Taylor expansion of \(\tan t\) and \(\log\sec t\) at zero.

For \(h=1\), the one-step law is a permutation of \((1-p,p,0)\). Directly, \(d_1(p)=\frac12\{|1-p-1/3|+|p-1/3|+1/3\}\), which attains \(1/3\) exactly when \(1/3\le p\le2/3\).

## Verification

The accompanying standalone `verify.py` evaluates the exact binomial residue distribution against the Fourier expression for every test probability on a \(1/100\) grid at horizons \(1\) through \(18\), and compares the analytic optimum against \(1001\)-point parameter grids at horizons \(2\) through \(60\). It also checks both predicted optimizers and the exceptional one-step interval. These checks pass; they are consistency experiments and **not** substitutes for the all-horizon proof above. The direct case \(h=2\) yields \(p_2^+=1/\sqrt3\) and \(d_2(p_2^+)=\frac{2\sqrt3-3}{3}\) numerically \(0.154700538\ldots\); the spectral-optimal choice has distance \(1/6\).

## Relationship to prior work

Boyd–Diaconis–Xiao optimize the second-largest eigenvalue modulus for *symmetric* stochastic transition matrices; the exact finite-horizon total-variation objective here is distinct, and this directed family is generally nonreversible. Gerencsér–Hendrickx–Van Dooren study spectral-gap optimization on finite cycles, not this finite-horizon variational problem. Gerencsér studies nonreversible mixing with a randomly **added edge** on longer cycles; that model differs from the three-state two-action transition family here. Olesker-Taylor–Zanetti develop general geometric bounds for fastest mixing, rather than an exact finite-time optimizer in this oriented triangle family. This result is an all-horizon exact optimization within the explicitly defined one-parameter family, not a general optimizer among arbitrary three-state chains.

## Limitations

The finding is limited to the directed three-state cycle with homogeneous stay-or-advance transitions. It does not prove uniqueness of the optimum over all doubly stochastic three-by-three transition matrices, nor global control of mixing-time thresholds at arbitrary tolerances. Prior-art coverage was compared in available source material, but complete bibliographic priority cannot be certified; a 2011 paper on mixing times on cycles was not fully accessible during the source review.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://doi.org/10.1137/S0036144503423264
2. B. Gerencsér, J. Hendrickx and P. Van Dooren, *Spectral gap of Markov chains on a cycle*, https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf
3. B. Gerencsér, *Analysis of a non-reversible Markov chain speedup by a single edge*, arXiv:1905.03223 (first public 2019-05-08), https://arxiv.org/abs/1905.03223
4. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, arXiv:2111.05816, https://arxiv.org/abs/2111.05816
5. B. Gerencsér, *Markov chain mixing time on cycles*, Stochastic Processes and their Applications 121 (2011), 2553–2570.
