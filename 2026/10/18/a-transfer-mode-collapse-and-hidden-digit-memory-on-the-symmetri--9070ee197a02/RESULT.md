# A transfer-mode collapse and hidden digit memory on the symmetric-doubling frequency plateau

## Finding
For the symmetric doubling maps introduced by Dajani and Kalle, the interval \(4/3\leq\alpha\leq3/2\) supports an exact two-function Perron–Frobenius closure. For \(4/3\leq\alpha<3/2\), it has a nonstationary eigenmode with eigenvalue \(-1/2\); at \(\alpha=3/2\) the two functions become identical and this particular mode vanishes. Every probability density in their convex hull relaxes to the invariant density by exactly a factor \(2^{-n}\) in total variation after \(n\) steps, with alternating sign of the deviation.

Throughout this same interval the stationary signed digits \(D_n\in\{-1,0,1\}\) have constant one-letter probabilities \((1/6,2/3,1/6)\), but their ordered adjacent-pair probabilities are
\[
\big(\Pr(D_0=i,D_1=j)\big)_{i,j=-1,0,1}
=\begin{pmatrix}a&b&0\\b&c&b\\0&b&a\end{pmatrix},
\quad a=\frac{3-2\alpha}{12\alpha},\quad
b=\frac{4\alpha-3}{12\alpha},\quad c=\frac{1}{2\alpha}.
\]
For every \(4/3\leq\alpha<3/2\), the stationary digit process is **not** a one-step Markov chain. At \(\alpha=3/2\), it **is** the classical stationary nonadjacent signed-digit Markov chain, with transition matrix (in order \(-1,0,1\))
\[
\begin{pmatrix}0&1&0\\1/4&1/2&1/4\\0&1&0\end{pmatrix}.
\]
The one-step conditional Shannon entropy \(H_1(\alpha)=H(D_1\mid D_0)\) is strictly decreasing on \([4/3,3/2]\), from approximately \(0.78463412\) to \(\log 2\). This is a **one-step conditional entropy**, not an assertion about the Kolmogorov–Sinai entropy or the full entropy rate.

## Assumptions and scope
For \(\alpha\in[4/3,3/2]\), define \(S_\alpha:[-1,1]\to[-1,1]\) by
\[
S_\alpha(x)=\begin{cases}
2x+\alpha,&-1\le x<-1/2,\\
2x,&-1/2\le x\le1/2,\\
2x-\alpha,&1/2<x\le1.
\end{cases}
\]
Let \(\mathcal L_\alpha\) be its Perron–Frobenius operator relative to Lebesgue measure and \(\mu_\alpha\) its unique absolutely continuous invariant probability (existence and uniqueness are established in the originating work). Under \(X_0\sim\mu_\alpha\), put \(X_{n+1}=S_\alpha(X_n)\) and \(D_n=-1,0,1\) according as \(X_n\) lies in the left, middle or right branch. Endpoints of cells are immaterial to these absolutely continuous laws. All entropy logarithms are natural.

Set \(c_\alpha=\alpha-1\), \(p_\alpha=2-\alpha\), \(r_\alpha=2\alpha-2\) and \(I_t(x)=\mathbf 1_{\{|x|<t\}}\). Note \(0<c_\alpha\le p_\alpha\le r_\alpha\le1\). Define \(g_0=1+I_{c_\alpha}\), \(g_1=I_{p_\alpha}+I_{r_\alpha}\), and
\[
q_t(x)=\frac{(1-t)g_0(x)+t g_1(x)}{2\alpha},\qquad 0\le t\le1.
\]
The functions \(q_t\) are probability densities; the claim about relaxation is restricted to these densities and does not assert a full transfer-operator spectrum.

## Proof
**1. Exact transfer closure.** The three inverse branches give, almost everywhere on \([-1,1]\),
\[
(\mathcal L_\alpha f)(x)=\frac12\left[f(x/2)+\mathbf1_{(-p_\alpha,c_\alpha)}(x)f((x-\alpha)/2)+\mathbf1_{(-c_\alpha,p_\alpha)}(x)f((x+\alpha)/2)\right].
\]
Direct comparisons of the branch images, using \(0<c_\alpha\le p_\alpha\le r_\alpha\le1\), yield
\[
\mathcal L_\alpha 1=\tfrac12(1+I_{c_\alpha}+I_{p_\alpha}),\qquad
\mathcal L_\alpha I_{c_\alpha}=\tfrac12 I_{r_\alpha},\qquad
\mathcal L_\alpha(I_{p_\alpha}+I_{r_\alpha})=1+I_{c_\alpha}.
\]
For the third identity, both central inverse branches contribute \(1\) in total, and the four relevant outer-image intervals contribute exactly \(\mathbf1_{\{|x|<c_\alpha\}}\); their inner meeting points are negatives of one another and their unions cover \((-c_\alpha,c_\alpha)\) twice before the outer-branch factor \(1/2\). These identities also hold at the two parameter endpoints, with zero-length pieces omitted. Consequently,
\[
\boxed{\mathcal L_\alpha g_0=\tfrac12(g_0+g_1),\qquad \mathcal L_\alpha g_1=g_0.}
\]
Both \(g_i\) integrate to \(2\alpha\). The normalized fixed density is
\[
h_\alpha=\frac{g_0+g_1/2}{3\alpha}=q_{1/3}.
\]
Its invariance follows from the displayed operator identities, so uniqueness identifies it with the Dajani–Kalle invariant density. The coefficient update is \(t\mapsto(1-t)/2\). Iteration gives
\[
\boxed{\mathcal L_\alpha^n q_t=q_{1/3+(-1/2)^n(t-1/3)}},\qquad n=0,1,2,\ldots .
\]
The total-variation equality follows by homogeneity of the difference from \(q_{1/3}\). For \(\alpha<3/2\), \(g_0-g_1\) is nonzero (on \(r_\alpha<|x|<1\) it equals \(1\)), and \(\mathcal L_\alpha(g_0-g_1)=-\frac12(g_0-g_1)\). At \(\alpha=3/2\), \(c_\alpha=p_\alpha=1/2\) and \(r_\alpha=1\), so \(g_0=g_1\) almost everywhere; this *specific* two-function eigendirection collapses. No absence of \(-1/2\) in other spaces is asserted.

**2. Exact two-letter law.** The density is even and equals \(1/\alpha\), \(2/(3\alpha)\), \(1/(2\alpha)\), \(1/(3\alpha)\) on successive regions \(0<|x|<c_\alpha\), \(c_\alpha<|x|<p_\alpha\), \(p_\alpha<|x|<r_\alpha\), \(r_\alpha<|x|<1\). Integrating over \([-1/2,1/2]\) gives exactly \(2/3\); symmetry gives probability \(1/6\) to each nonzero digit. Opposite nonzero digits cannot be adjacent: for \(x>1/2\), \(S_\alpha(x)>1-\alpha\ge-1/2\), and the negative-side case is symmetric. Two successive positive digits occur exactly for
\[
x>\frac{\alpha+1/2}{2}=\frac\alpha2+\frac14.
\]
This cutoff lies at or beyond \(r_\alpha\), since their difference is \((9-6\alpha)/4\ge0\). Thus the density throughout that positive-positive cylinder is \(1/(3\alpha)\), and its measure is \((3-2\alpha)/(12\alpha)=a\). Reflection gives the negative-negative probability. Stationarity then gives the four \(b=1/6-a\) entries and the remaining central entry \(c=2/3-2b=1/(2\alpha)\), proving the matrix.

**3. Sharp Markov boundary.** For a positive digit, the next state is at most \(p_\alpha=2-\alpha\). If that next state is again positive, the third state is at most \(2p_\alpha-\alpha=4-3\alpha\le0\). Hence the word \((1,1,1)\) never occurs. For \(\alpha<3/2\), however, the positive-positive cylinder has positive probability \(a>0\). A stationary first-order Markov chain with \(\Pr(D_0=1,D_1=1)>0\) must assign \(\Pr(D_0=D_1=D_2=1)>0\), a contradiction. At \(\alpha=3/2\), the invariant density is constant on each of the three digit cells, and each allowed branch-cylinder \(\{D_0=i,D_1=j\}\) maps affinely *onto the full cell* for digit \(j\), with constant absolute slope \(2\). Inductively, conditional on any finite admissible past ending in cell \(j\), the state is uniformly distributed on that cell. Future one-digit probabilities consequently depend only on \(j\), giving the displayed Markov transition matrix. This endpoint behavior is classical and is not claimed as a new result.

**4. Strict conditional-entropy variation.** Write \(a,b,c\) as in the Finding and use \(0\log0=0\). Since the marginals are \((1/6,2/3,1/6)\),
\[
H_1(\alpha)=-2a\log(6a)-2b\log(6b)-2b\log(3b/2)-c\log(3c/2).
\]
For \(4/3\le\alpha<3/2\), differentiating and collecting the terms (the sum of all probabilities is constant) yields
\[
\boxed{H_1'(\alpha)=\frac1{2\alpha^2}\log\frac{ac}{b^2}<0.}
\]
Indeed \(b^2-ac=(16\alpha^2-12\alpha-9)/(144\alpha^2)>0\) on this interval. Continuity and the explicit endpoint matrix give \(H_1(3/2)=\log2\), with \(H_1(4/3)\approx0.7846341196\). This completes the stated strict monotonicity.

## Verification
Run the standalone, standard-library-only `verify.py` using `python3 verify.py`. It constructs the literal inverse-branch transfer operator, integrates the invariant density against all nine two-letter cylinders by exact rational interval subdivision, and tests the three transfer identities on every induced affine partition cell at 32 rational parameter values, including both endpoints. It reports `CHECK_OK parameters 32 exact_or_derived_checks 1343`. These finite tests do not certify the continuum of parameters; the exact branch-interval algebra and the above proof establish that continuum.

## Relationship to prior work
Dajani and Kalle introduce these maps, establish uniqueness of the absolutely continuous invariant probability, give an explicit indicator-function density formula and prove that the zero-digit frequency is \(2/3\) throughout the larger interval \([6/5,3/2]\). Their two-step matching interval and density formula underlie the present calculation; neither the invariant density nor the constant digit marginals is claimed as new. The additional assertions here are the two-function transfer closure and signed relaxation mode, the **joint** digit law and strict conditional-entropy variation, and the sharp non-Markov region below the classical endpoint. Dajani, Kraaikamp and Liardet already give the three-state stationary Markov structure for classical nonadjacent signed-binary expansions. Their endpoint transition matrix is acknowledged rather than newly claimed. Dajani and Sanderson study a different symmetric *golden-base* map, not the slope-two family in this theorem. Existing general transfer-operator theory supplies the general formalism; the exact parameter-uniform two-function identities are obtained from the particular branches above.

## Limitations
The invariant two-function subspace is not a classification of the entire Perron–Frobenius spectrum. Its eigenmode degenerates at \(\alpha=3/2\) only within this explicitly defined subspace. The conditional entropy is a one-step statistic, not the full entropy rate. The result concerns \([4/3,3/2]\), not the entire zero-frequency plateau \([6/5,3/2]\). An equivalent earlier calculation in a different coding cannot be excluded without further independent priority investigation.

## References
1. Karma Dajani and Charlene Kalle, *Invariant measures, matching and the frequency of 0 for signed binary expansions*, arXiv `1703.06335v1`, first public March 18, 2017; *Publications of the Research Institute for Mathematical Sciences* 56(4), DOI `10.4171/PRIMS/56-4-2`. In particular the symmetric doubling map, the transfer-operator formula, invariant-density construction, and Theorem 5.2.
2. Karma Dajani, Cor Kraaikamp and Pierre Liardet, *Ergodic properties of signed binary expansions*, *Discrete and Continuous Dynamical Systems* 15(1) (2006), 87–119, DOI `10.3934/dcds.2006.15.87` (the classical three-state Markov process).
3. Karma Dajani and Slade Sanderson, *Ergodic properties of a parameterised family of symmetric golden maps: the matching phenomenon revisited*, arXiv `2301.08623v1` (2023), for comparison with a distinct base and matching setting.
