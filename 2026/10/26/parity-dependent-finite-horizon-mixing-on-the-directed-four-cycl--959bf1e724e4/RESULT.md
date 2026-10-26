# Parity-dependent finite-horizon mixing on the directed four-cycle

## Finding
Let \(d_h(p)\) be the total-variation distance to the uniform law after \(h\) steps of the clockwise lazy random walk with move probability \(p\) on four vertices. At every **even** integer \(h\ge2\), the unique minimizer is \(p=1/2\) and the minimum is \(2^{-h/2-1}\). At every **odd** integer \(h\ge3\), \(p=1/2\) is instead a strict local maximum; global minimizing parameters occur in reflected off-center pairs. Writing \(m_h=\min_{0\le p\le1}d_h(p)\),
\[
\frac{m_h}{d_h(1/2)}=\frac1{\sqrt2}+O(h^{-1})\qquad (h\longrightarrow\infty,\ h\text{ odd}).
\]
In particular, the unique eigenvalue-modulus minimizer is optimal in total variation precisely at even horizons in the stated range, and finite-horizon optimization achieves asymptotically about 29.3 percent relative improvement over this choice at odd horizons.

## Assumptions and scope
The state space is \(\mathbb Z/4\mathbb Z\), and \(S\) advances one site clockwise. Let \(P_p=(1-p)I+pS\), \(0\le p\le1\). Each of the four starting states gives the same total-variation distance \(d_h(p)\) from the stationary uniform probability \(U\), by cyclic symmetry. The horizon is an integer \(h\ge2\); statements about odd horizons start at \(h=3\). At the two endpoint parameters the walk is nonergodic, but its finite-time distance is still defined. No assertion of uniqueness or closed-form exact locations of odd-horizon global minimizers is made.

## Proof
Write \(\lambda=1-p+ip\), \(B=(1-2p)^h\), \(C=\operatorname{Re}\lambda^h\), and \(T=\operatorname{Im}\lambda^h\). Fourier inversion on the cyclic group yields the four signed mass deviations from \(1/4\), in cyclic order,
\[
\frac14(B+2C,\,-B+2T,\,B-2C,\,-B-2T).
\]
Using \(|x+y|+|x-y|=2\max(|x|,|y|)\), we obtain the exact formula
\[
 d_h(p)=\frac{\max(|B|,2|C|)+\max(|B|,2|T|)}4.
\tag{1}
\]
In particular, with \(r=|\lambda|\) and \(\theta=\arg\lambda\) (using the first quadrant including its endpoints),
\[
 d_h(p)\ge\frac{|C|+|T|}{2}
 =\frac{r^h}{2}\bigl(|\cos(h\theta)|+|\sin(h\theta)|\bigr)
 \ge\frac{r^h}2\ge 2^{-h/2-1},
\tag{2}
\]
since \(r^2=1/2+2(p-1/2)^2\). For \(p\ne1/2\), the last inequality is strict. At \(p=1/2\), \(B=0\), \(r=1/\sqrt2\) and \(\theta=\pi/4\). If \(h\) is even, \(h\theta\) is an integer multiple of \(\pi/2\); then equality holds throughout (2). This proves the even-horizon minimum and uniqueness.

If \(h\) is odd, \(h\pi/4\) is an odd multiple of \(\pi/4\), and \(d_h(1/2)=r^h/\sqrt2\). Put \(u=p-1/2\). Around \(u=0\), \(B=O_h(|u|^h)\) and both \(|C|\) and \(|T|\) remain nonzero, so in (1) both maxima select the Fourier terms. Moreover,
\[
 r=2^{-1/2}(1+2u^2+O(u^4)),\qquad
 \theta=\pi/4+2u+O(u^3).
\]
The absolute-value trigonometric sum near the odd multiple of \(\pi/4\) equals \(\sqrt2\cos(2hu+O_h(u^3))\). Consequently,
\[
\frac{d_h(1/2+u)}{d_h(1/2)}
 =1-2h(h-1)u^2+O_h(u^4),
\tag{3}
\]
so the center is a strict local maximum for \(h\ge3\). Continuity ensures a global minimum, symmetry of the binomial increment count gives \(d_h(p)=d_h(1-p)\), and \(d_h(0)=d_h(1)=3/4>d_h(1/2)\). Thus minimizing points are strictly interior, noncentral, and come in reflected pairs.

For odd \(h\ge3\), set \(\varepsilon_h=\pi/(4h)\) and
\[
 p_h=\frac{1+\tan\varepsilon_h}{2}.
\]
Then \(0<p_h<1\), \(\arg(1-p_h+ip_h)=\pi/4+\varepsilon_h\), so \(h\arg\lambda\) is a multiple of \(\pi/2\). Also \(|\lambda|=2^{-1/2}\sec\varepsilon_h\) and \(|1-2p_h|=\tan\varepsilon_h\), with \(|B|<2|\lambda|^h\). Hence (1) gives the exact witness distance
\[
 d_h(p_h)=2^{-h/2-1}\sec^h\varepsilon_h
   +\frac14\tan^h\varepsilon_h.
\tag{4}
\]
The universal bound (2), together with \(\sec^h(\pi/(4h))=1+O(h^{-1})\) and \(2^{h/2}\tan^h(\pi/(4h))=o(h^{-1})\), implies
\[
 m_h=2^{-h/2-1}\bigl(1+O(h^{-1})\bigr).
\]
Since \(d_h(1/2)=\sqrt2\,2^{-h/2-1}\) for odd \(h\), this completes the claimed ratio. Finally, the nontrivial Fourier eigenvalues are \(1-2p\), \(1-p+ip\), and its conjugate; their maximum modulus is uniquely minimized at \(p=1/2\), because \(|1-p+ip|\) is uniquely minimized there and bounds the spectral maximum below.

## Verification
The standalone \(`verify.py`\) computes cyclic transition distributions and Fourier-inverted distributions using exact rational arithmetic for every integer horizon from 1 to 30 and 61 rational parameters on the mesh \(p=j/60\), totaling 1,830 comparisons. It additionally checks even-horizon identities and odd-horizon strict central improvements on finite grids and numerically evaluates the explicit phase-aligned witness. Run \(`python verify.py`\) with Python 3; no nonstandard packages are required. These finite checks supplement, but do not replace, the analytic proof above.

## Relationship to prior work
Finite-state mixing commonly uses spectral decay as a proxy for total variation. Collevecchio–Griffiths (2020) studies critical mixing of walks on high-dimensional hypercubes; Olesker-Taylor–Zanetti (2021) develops geometric/spectral bounds for fastest-mixing Markov chains. Both concern different chain classes and optimization objectives from the exact nonreversible directed four-cycle finite-horizon parameter problem here. Existing results on \(\ell^4\) contraction for four-state cyclic convolutions optimize a different operator norm, and do not immediately imply the total-variation parity phenomenon. The underlying Fourier diagonalization is standard; novelty, if confirmed, resides in the **all-horizon parity classification** and sharp odd-horizon asymptotic benefit.

## Limitations
This gives no closed formula or uniqueness classification for the exact optimizer at odd finite horizons; the witness need not be an exact minimizer. It is specific to the directed four-cycle and its one-parameter lazy clockwise kernel, not arbitrary Markov chains. Historical priority is not certified: unidentified specialized exact mixing results may overlap. A finite computational verification is not a proof of an infinite-horizon statement.

## References
1. A. Collevecchio and R. Griffiths, *Three steps mixing for general random walks on the hypercube at criticality*, arXiv:2002.09059 (first publicly available 2020-02-20), https://arxiv.org/abs/2002.09059.
2. S. Olesker-Taylor and M. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, arXiv:2111.05816 (first publicly available 2021-11-10), https://arxiv.org/abs/2111.05816.
