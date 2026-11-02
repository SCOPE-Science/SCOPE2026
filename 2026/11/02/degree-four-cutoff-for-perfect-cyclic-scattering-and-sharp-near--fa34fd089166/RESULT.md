# Degree-four cutoff for perfect cyclic scattering and sharp near-rotational leakage in quantum stars

## Finding

Consider the interpolating unitary vertex family of Exner, Turek and Tater on an \(n\)-lead quantum star, with \(n\ge 2\), interpolation \(0\le t\le1\), real endpoint delta-strength \(\alpha\), and on-shell momentum \(k>0\). Let \(R\) denote the cyclic routing permutation with \(R_{j,j+1}=1\) (indices modulo \(n\)). A *perfect deterministic router* is a scattering matrix for which every incident lead exits on a single lead with probability one; phase factors and a different cyclic destination are initially allowed.

**Exact degree classification.** For \(n=2\), perfect deterministic routing occurs precisely when \(t=1\) or \(\alpha=0\), at every \(k>0\). For each \(n\ge3\), it occurs precisely in either of the following situations:

1. \(t=1\), \(k=1\), with arbitrary \(\alpha\); or
2. \(\alpha=0\), \(0<t<1\), \(n\in\{3,4\}\), and
   \[
   k=\begin{cases}
       \frac{1}{\sqrt3}\cot(\pi t/6), & n=3,\\
       \cot(\pi t/4), & n=4.
      \end{cases}
   \]

In all these cases the matrix equals \(R\), without any residual global phase or nontrivial alternative permutation. In particular, no \(n\ge5\) vertex with \(0\le t<1\) can be a deterministic router, at any real \(\alpha\) or positive momentum. At the Kirchhoff endpoint the three- and four-lead tuning momenta diverge like \(t^{-1}\), so their tuned energies diverge like \(t^{-2}\).

**Sharp, optimized high-degree leakage.** Fix \(n\ge5\) and \(\alpha=0\), and denote the probability of the desired cyclic output by \(P_n(t,k)=|\mathcal S_{0,1}(t,k)|^2\). There is an \(\varepsilon_n>0\) such that for \(1-\varepsilon_n<t\le1\) this probability has a unique global maximizer in \(k>0\), and as \(\delta=1-t\downarrow0\),
\[
 k_{\mathrm{opt}}(t)=1+d_n\delta+O_n(\delta^2),\qquad
 1-\max_{k>0}P_n(t,k)=C_n\delta^2+O_n(\delta^3).
\]
With \(h=\lfloor(n-1)/2\rfloor\), \(a_j=\pi j/n\), and \(v_j=\pi/2-a_j\) for \(1\le j\le h\), the exact coefficients are
\[
 d_n=\frac{2\sum_{j=1}^{h}v_j\sin(2a_j)}{\sum_{j=1}^{h}\sin^2(2a_j)},\quad
 C_n=\frac8n\left(\sum_{j=1}^{h}v_j^2-\frac{\left(\sum_{j=1}^{h}v_j\sin(2a_j)\right)^2}{\sum_{j=1}^{h}\sin^2(2a_j)}\right)>0.
\]
For orientation, \(C_5=0.083356948827\ldots\) and \(C_6=0.182770451872\ldots\). Thus the higher-degree obstruction persists even after optimal momentum calibration, with a calculable strictly positive leading loss.

## Assumptions and scope

The star has \(n\) semi-infinite leads and the self-adjoint condition \((U-I)\Psi+i(U+I)\Psi'=0\) in units where the vertex length scale is one. All momentum and energy statements use this convention. Write \(\gamma=2\arctan(\alpha/n)\in(-\pi,\pi)\). The unitary \(U=U_{n,\alpha}(t)\) is the circulant matrix with Fourier eigenvalues
\[
 \lambda_0=e^{-i(1-t)\gamma},\qquad
 \lambda_j=-e^{i\pi t(2j/n-1)}\quad(1\le j<n).
\]
The exact scattering matrix and its Fourier eigenvalues are
\[
 \mathcal S(k)=\big((k+1)I+(k-1)U\big)^{-1}\big((k-1)I+(k+1)U\big),\qquad
 \mu_j=\frac{k-1+(k+1)\lambda_j}{k+1+(k-1)\lambda_j}.
\]
The matrix is unitary and circulant for all listed real parameters. Perfect deterministic routing permits any exit permutation and unit-modulus phases before the classification is imposed. The optimized leakage assertion varies momentum only and fixes \(\alpha=0\).

## Proof

**1. Rigidity of a circulant deterministic router.** A circulant matrix whose squared-modulus matrix is a permutation is necessarily \(e^{i\chi}R^m\). For \(1\le j\le h\), the Fourier eigenvalues obey \(\lambda_{n-j}=\overline{\lambda_j}\) and \(\mu_{n-j}=\overline{\mu_j}\), so \(\mu_j\mu_{n-j}=1\). If \(\mathcal S=e^{i\chi}R^m\), Fourier comparison therefore gives \(e^{2i\chi}=1\). Since \(\mu_0\) cannot equal \(-1\) at any positive \(k\) when \(|(1-t)\gamma|<\pi\), necessarily \(\chi=0\) and \(\mu_0=1\). The latter is equivalent to \(t=1\) or \(\alpha=0\).

At \(t=0\) and \(n\ge3\), all the Fourier eigenvalues \(\mu_j\) for \(j\ge1\) equal \(-1\). No \(R^m\) can have simultaneously \(\mu_1=\mu_2=-1\), so deterministic routing is impossible there. For \(t>0\), all \(\mu_j\) with \(1\le j\le h\) lie strictly in the upper half-plane, because their corresponding coupling eigenvalues are on the upper open unit semicircle and the Möbius transform preserves its sign of imaginary part. If \(\mathcal S=R^m\), then \(\mu_1=e^{2\pi im/n}\) forces \(1\le m<n/2\). If \(m\ge2\), taking \(j=\lceil n/(2m)\rceil\le h\) makes \(e^{2\pi imj/n}\) real negative or lower-half-plane, a contradiction. Therefore \(m=1\).

The degree-two case follows directly: \(\lambda_1=-1\) for all \(t\), and \(\lambda_0=1\) precisely if \(\alpha=0\) or \(t=1\). Then \(\mu_0=1\), \(\mu_1=-1\) at all positive momenta, giving \(\mathcal S=R\).

**2. Modal tuning and degree cutoff.** For \(1\le j\le h\), put \(a_j=\pi j/n\) and \(v_j=\pi/2-a_j\). For \(t>0\), direct substitution gives
\[
 \mu_j=\frac{k+i\cot(tv_j)}{k-i\cot(tv_j)}
       =\exp\!\big(2i\arctan(\cot(tv_j)/k)\big).
\]
At even degree the middle eigenvalue is always \(\mu_{n/2}=-1\). Thus \(\mathcal S=R\) if and only if \(\mu_0=1\) and
\[
   k=K_j(t):=\frac{\tan v_j}{\tan(tv_j)}
       \qquad(1\le j\le h).
\]
If \(t=1\), all these values equal one. If \(0<t<1\), then \(K_j(t)\) is strictly increasing as a function of \(v_j\), since
\[
 \frac{d}{dv}\log\frac{\tan v}{\tan(tv)}
       =\frac{2}{\sin(2v)}-\frac{2t}{\sin(2tv)}>0,
\]
using strict decrease of \(\sin x/x\) on \((0,\pi)\). Consequently one equation can be met for \(h=1\), i.e. \(n=3,4\), but two cannot be met when \(h\ge2\), i.e. \(n\ge5\). The explicit \(n=3,4\) formulas and small-\(t\) behavior follow from \(K_1\).

**3. Optimized leakage.** Set \(\alpha=0\), \(\delta=1-t\), and write \(k=1+\xi\). The residual Fourier phase of the \(j\)-th mode relative to \(R\) is
\[
 \eta_j=2\arctan(\cot(tv_j)/k)-2a_j
      =2v_j\delta-\sin(2a_j)\xi+O_n((|\delta|+|\xi|)^2).
\]
The target amplitude is real and exactly
\[
  \mathcal S_{0,1}=\frac{n-2h+2\sum_{j=1}^{h}\cos\eta_j}{n}.
\]
Therefore, uniformly in a neighborhood of \((\delta,\xi)=(0,0)\),
\[
 1-P_n(1-\delta,1+\xi)
  =\frac2n\sum_{j=1}^{h}\big(2v_j\delta-\sin(2a_j)\xi\big)^2
    +O_n((|\delta|+|\xi|)^3).
\]
The positive quadratic coefficient in \(\xi\) gives a unique analytic local maximizer with \(\xi=d_n\delta+O_n(\delta^2)\) and loss coefficient \(C_n\) as claimed.

For globality, at \(t=1\) the first two steps prove \(P_n(1,k)=1\) only at \(k=1\). The limits at \(k\downarrow0\) and \(k\to\infty\) have target probability no larger than \((2/n)^2<1\), uniformly for \(t\) near one. Compactifying the momentum half-line shows every global maximizer approaches one; the strict local maximum is therefore also the unique global maximum for all sufficiently small \(\delta\). Finally, the Cauchy–Schwarz inequality is strict in \(C_n\) for \(h\ge2\), because \(v/\sin(2v)\) is strictly increasing on \((0,\pi/2)\), so the vectors \((v_j)\) and \((\sin2a_j)\) are not proportional.

## Verification

The standalone `CHECK.py` reconstructs Fourier-mode scattering eigenvalues and independently inverts the finite scattering matrix. It compares all corresponding target amplitudes for multiple degrees and parameters; tests exact cyclic routing at the predicted momenta; and checks sample high-degree leakage asymptotics against numerical optimization. Running `python3 CHECK.py` prints `VERIFY_OK 106 checks` and reference coefficients for degrees five and six. These finite computations corroborate the formulas; the all-degree uniqueness and positivity claims follow from the preceding analytic argument, not extrapolation from tests.

## Relationship to prior work

Exner, Turek and Tater (2018) define the entire interpolating family and give its exact on-shell scattering matrix, modal eigenvalues and explicit degree-four entries. Exner and Tater (2017) establish the preferred-orientation endpoint and its perfect cyclic scattering at the special momentum. Exner and Pekař (2024) analyze spectral bands in quantum chain graphs carrying this same interpolating coupling. These results supply the foundational scattering formulas and are not claimed as new.

The findings proved here concern the *existence classification over all degrees, momenta and delta strengths* of deterministic routing inside this family, and the *sharp, globally momentum-optimized first leakage coefficient* when the interpolation is perturbed away from the pure preferred-orientation endpoint. Those assertions are not stated by the cited papers, although they are nontrivial consequences of the published modal formulas. No priority assertion beyond the inspected sources is implied.

## Limitations

The coupling interpolation and star geometry are fixed. The degree cutoff does not rule out perfect circulation with other self-adjoint vertex couplings or with additional graph structure. The leakage coefficient is established for zero delta-strength and for \(t\) approaching one; its proof does not determine the full global optimum for every \(0<t<1\), or when both momentum and delta-strength vary jointly. Numerical checks are not substitutes for the all-parameter analytic steps. Publication priority beyond the identified and inspected sources has not been independently certified.

## References

1. P. Exner, O. Turek, M. Tater, *A family of quantum graph vertex couplings interpolating between different symmetries*, first public 2018-04-04, [arXiv:1804.01414](https://arxiv.org/abs/1804.01414), especially Sections 3 and 5.
2. P. Exner, M. Tater, *Quantum graphs with vertices of a preferred orientation*, first public 2017-10-07, [arXiv:1710.02664](https://arxiv.org/abs/1710.02664), especially Section 2.
3. P. Exner, J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, first public 2024-03-14, [arXiv:2403.09457](https://arxiv.org/abs/2403.09457), especially Section 2.
