# A logarithmic endpoint derivative gap for the Ehrenfest semigroup

## Finding
Let \(n=2m\ge 2\) and let \(Q_n\) be the continuous-time Ehrenfest generator on functions on \(\{0,\ldots,n\}\):
\[
(Q_nf)(i)=(n-i)[f(i+1)-f(i)]+i[f(i-1)-f(i)],
\]
where an absent endpoint term is omitted. Put \(T_n(t)=e^{tQ_n}\). All \(\ell^1\) and \(\ell^\infty\) operator norms below use **unweighted counting measure** on the \(n+1\) states. Set \(a=e^{-2t}\) and \(c_n=(n+1)\binom{n}{m}/2^n\).

**Exact finite-time column norm.** For every \(t>0\),
\[
\boxed{\|T_n(t)\|_{\ell^1\to\ell^1}
=\frac{c_n}{a}\int_0^a(1-s^2)^m\,ds.}
\]
The unique maximizing column is the central state \(m\). The norm increases strictly from \(1\) at time zero to \(c_n\) at infinite time, and \(c_n\sim\sqrt{2n/\pi}\). Its derivative has the exact expression
\[
\frac{d}{dt}\|T_n(t)\|_{\ell^1\to\ell^1}
=2c_n\left[\frac1a\int_0^a(1-s^2)^m\,ds-(1-a^2)^m\right]>0.
\]

**Logarithmic separation of endpoint time-weighted derivatives.** Write
\[
M_{r,n}=\sup_{t>0}t\|Q_nT_n(t)\|_{\ell^r\to\ell^r}\quad(r\in\{1,\infty\}).
\]
Then
\[
\boxed{M_{\infty,n}=(\gamma+o(1))\sqrt n,\qquad
M_{1,n}\ge(\beta+o(1))\sqrt n\log n,}
\]
where the explicit positive constants are
\[
\gamma=\max_{t>0}\sqrt{\frac8\pi}\frac{t}{\sqrt{e^{4t}-1}}
\approx0.321045745272253,
\qquad
\beta=\frac12\sqrt{\frac2\pi}\left(\int_0^1 e^{-u^2/2}\,du-e^{-1/2}\right)
\approx0.099374021549400.
\]
The unique maximizing positive time in the formula for \(\gamma\) solves \(1-e^{-4t}=2t\). Consequently,
\[
\boxed{\liminf_{\substack{n\to\infty\\n\text{ even}}}
\frac{M_{1,n}}{M_{\infty,n}\log n}
\ge\frac{\beta}{\gamma}\approx0.309532280096497.}
\]
The logarithmic lower bound is a new counting-norm phenomenon; the known full Boolean-cube endpoint identity used to establish \(\gamma\) is not claimed as new.

## Assumptions and scope
The result concerns finite **even** positive integers \(n\), the generator above with each bit flipping at rate one, continuous time \(t>0\), and ordinary unweighted state-coordinate norms. The Ehrenfest process is the Hamming-weight lumping of independent symmetric two-state chains; its stationary distribution is \(\pi_j=2^{-n}\binom nj\). Stationary-weighted \(\ell^1\) is a different norm and does not display the same column growth. The asymptotic statements concern \(n\to\infty\) through even integers. The claim supplies a lower bound, **not** a matching asymptotic or an exact finite-dimensional formula, for \(M_{1,n}\).

## Proof
**1. Transition generating functions and the central-column maximum.** Put \(p=(1-a)/2\) and \(q=(1+a)/2\). For a chain starting with \(i\) occupied bits, each initial occupied bit contributes probability-generating polynomial \(A(z)=p+qz\), and each initially unoccupied bit contributes \(B(z)=q+pz\). Thus, with \(P_{ij}(t)=T_n(t)_{ij}\),
\[
\sum_{j=0}^nP_{ij}(t)z^j=A(z)^iB(z)^{n-i}.
\]
The column-sum polynomial, where \(C_j(t)=\sum_{i=0}^nP_{ij}(t)\), is
\[
\sum_{j=0}^n C_j(t)z^j
=\sum_{i=0}^nA(z)^iB(z)^{n-i}
=\frac{B(z)^{n+1}-A(z)^{n+1}}{a(1-z)}.
\]
Hence \(C_j-C_{j-1}\) is \(a^{-1}\) times the difference between the \(j\)-th probability masses of \({\rm Bin}(n+1,p)\) and \({\rm Bin}(n+1,q)\). For \(0<p<q\), the ratio of these masses is \((p/q)^{2j-(n+1)}\). It exceeds one for \(j\le m\) and is below one for \(j\ge m+1\). Therefore \(C_m\) is the unique maximum for every \(t>0\). Since all transition entries are nonnegative, \(\|T_n(t)\|_{1\to1}=C_m(t)\).

**2. Exact integral and strict growth.** Let \(F(a)=\Pr\{{\rm Bin}(n+1,(1-a)/2)\le m\}\). Binomial symmetry and the preceding generating function give \(aC_m(t)=2F(a)-1\). Differentiating the finite binomial tail yields
\[
\frac{d}{da}\bigl(2F(a)-1\bigr)
=(n+1)\binom nm2^{-n}(1-a^2)^m=c_n(1-a^2)^m.
\]
At \(a=0\) this numerator vanishes, so integration gives the claimed exact formula. Writing \(h(s)=(1-s^2)^m\), we have
\[
C_m'(t)=2c_n\left[a^{-1}\int_0^ah(s)\,ds-h(a)\right]>0,
\]
because \(h\) is strictly decreasing. As \(a\downarrow0\) the bracketed average tends to one, giving the limiting column norm \(c_n\). Stirling's formula gives \(c_n\sim\sqrt{2n/\pi}\).

**3. Exact inherited infinity derivative norm.** The original Boolean cube transition kernel is a product of the two-state kernels and its derivative is translation invariant. The derivative of each microstate probability at Hamming distance \(k\) has the same sign as \(k-np\). Collapsing microstates into Hamming-weight shells cannot increase an absolute row sum. For the initial all-zero vertex, no opposite signs occur within one Hamming shell, so collapse preserves the full derivative row sum. Consequently
\[
\|Q_nT_n(t)\|_{\infty\to\infty}
=\frac{a}{pq}\mathbb E|K-np|
=2na\Pr\{{\rm Bin}(n-1,p)=\lfloor np\rfloor\},
\]
where \(K\sim{\rm Bin}(n,p)\). The last equality follows by telescoping the binomial mass identities \(k\binom nk=n\binom{n-1}{k-1}\) and \((n-k)\binom nk=n\binom{n-1}{k}\), including the integer-mean boundary case.

**4. Optimization of the infinity endpoint.** For fixed \(t>0\), the binomial local central limit theorem gives
\[
\frac{t}{\sqrt n}\|Q_nT_n(t)\|_{\infty\to\infty}
\longrightarrow\sqrt{\frac8\pi}\frac{t}{\sqrt{e^{4t}-1}}.
\]
This convergence is uniform on compact positive time intervals. Fourier inversion of the binomial characteristic function yields a uniform point-mass estimate \(\max_k\Pr\{{\rm Bin}(n-1,p)=k\}\le C/\sqrt{(n-1)pq}\) for \(n\ge2\). The resulting normalized envelope is bounded by a constant times \(t/\sqrt{e^{4t}-1}\), which tends to zero as \(t\downarrow0\) or \(t\to\infty\). The maximum therefore converges to \(\gamma\). Differentiation shows its unique positive maximizer satisfies \(1-e^{-4t}=2t\).

**5. A growing derivative lower bound.** At \(t_n=(\log n)/4\), we have \(a=n^{-1/2}\). Substitute \(u=\sqrt n\,s\) into the exact derivative of the central column. Dominated convergence, \(c_n/\sqrt n\to\sqrt{2/\pi}\), and \((1-u^2/n)^{n/2}\to e^{-u^2/2}\) show that
\[
\frac{C_m'(t_n)}{\sqrt n}\longrightarrow
2\sqrt{\frac2\pi}\left(\int_0^1e^{-u^2/2}\,du-e^{-1/2}\right)=4\beta.
\]
Since \(\|Q_nT_n(t)\|_{1\to1}\ge\left|\sum_i(Q_nT_n(t))_{im}\right|=C_m'(t)\), it follows that
\[
M_{1,n}\ge t_nC_m'(t_n)
=(\beta+o(1))\sqrt n\log n.
\]
Division by the established infinity-endpoint asymptotic gives the ratio bound.

## Verification
The accompanying pure-standard-library file `ehrenfest_endpoint_checker.py` independently constructs \(e^{tQ_n}\) by Poisson uniformization of the finite generator, computes absolute row and column sums, and compares them with the derived formulas at 36 finite parameter pairs. It makes 427 finite consistency comparisons and also tests the predicted rescaled derivative on seven larger even state spaces. All comparisons pass with the included numerical tolerances. Computation is a cross-check, not a proof of the asymptotic statements; the latter are derived above from exact identities, Stirling's formula, and binomial local limits.

Run with `python3 ehrenfest_endpoint_checker.py`.

## Relationship to prior work
Feinsilver and Kocik describe the Kac/Ehrenfest tridiagonal operator using Krawtchouk matrices; Kaplun gives continuous-time transition formulas and the binomial stationary law. Diaconis and Griffiths develop multivariate Krawtchouk spectral representations and Ehrenfest composition chains. These establish the transition and spectral machinery, not the present exact **unweighted column-sum amplification** and logarithmic separation between counting-\(\ell^1\) and \(\ell^\infty\) time-weighted derivative norms. The infinity endpoint calculation itself is classical on the full Boolean cube and is used as an input, not asserted to be novel.

## Limitations
The logarithmic \(\ell^1\) estimate is a lower bound; no matching universal upper coefficient is supplied. The exact finite-time \(\ell^1\) expression is proved for even \(n\); no odd-\(n\) variant is claimed. The spectral eigenvalues by themselves do not determine unweighted counting-norm amplification. Related work under total-variation or Ehrenfest-urn terminology may have considered equivalent column norms; the historical comparison is not an independent priority certification. No claim of computational verification for all \(n\) is made.

## References
- P. Feinsilver and J. Kocik, *Krawtchouk polynomials and Krawtchouk matrices*, arXiv:quant-ph/0702073 (first public preprint 2007-02-07), https://arxiv.org/abs/quant-ph/0702073.
- A. Kaplun, *Continuous time Ehrenfest process in term structure modelling*, arXiv:1003.6042 (2010), https://arxiv.org/abs/1003.6042.
- P. Diaconis and R. Griffiths, *An introduction to multivariate Krawtchouk polynomials and their applications*, arXiv:1309.0112 (2013), https://arxiv.org/abs/1309.0112.
- P. Diaconis and R. Griffiths, *Exchangeable pairs of Bernoulli random variables, Krawtchouk polynomials, and Ehrenfest urns*, 2012, DOI:10.1111/j.1467-842X.2012.00654.x.
- M. Voit, *Asymptotic distributions for the Ehrenfest urn and related random walks*, *Journal of Applied Probability* **33** (1996); historical full text not examined.
- H. Zhou and K. Lange, *Composition Markov chains of multinomial type*, *Advances in Applied Probability* **41** (2009), 270–291, DOI:10.1239/aap/1240319585; author-hosted full text: https://hua-zhou.github.io/media/pdf/ZhouLange09Multinomial.pdf.
