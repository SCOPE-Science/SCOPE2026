# Contact-rate resonance and a crossover law for SI completion on clique bouquets

## Finding

For a complete-infection SI process started at the common hub of a bouquet of \(m\) identical cliques, the completion time has an exact finite-network law and three sharply different extreme-value normalizations. Writing \(k\ge2\) for the number of nonhub vertices per clique, \(\beta>0\) for the hub-to-nonhub edge transmission rate, and \(\gamma\ge0\) for every nonhub-to-nonhub edge rate, define
\[
\lambda_j=(k-j)(\beta+j\gamma),\qquad j=0,\ldots,k-1.
\]
If \(D\) is the duration required to infect one clique's nonhub vertices after the initially infected hub, then
\[
D\overset{d}{=}\sum_{j=0}^{k-1}\operatorname{Exp}(\lambda_j),\quad
\mathbb E[e^{-sD}]=\prod_{j=0}^{k-1}\frac{\lambda_j}{\lambda_j+s},\quad
\Pr(T_m\le t)=\Pr(D\le t)^m.
\]
All exponentials appearing in the first sum and all petal durations are independent. Here \(T_m\) is the time when all \(mk\) nonhub vertices are infected.

For fixed \(\gamma\ne\beta\), let \(a=\min\{k\beta,\beta+(k-1)\gamma\}\), let \(j_*\in\{0,k-1\}\) be its unique index, and put
\[
C_{k,\beta,\gamma}=\prod_{j\ne j_*}\frac{\lambda_j}{\lambda_j-a}.
\]
For every real \(x\),
\[
\lim_{m\to\infty}\Pr\bigl(aT_m-\log m-\log C_{k,\beta,\gamma}\le x\bigr)
=\exp(-e^{-x}). \tag{1}
\]
At the contact-rate resonance \(\gamma=\beta\), two slow exponential stages coincide at \(a=k\beta\), and
\[
\lim_{m\to\infty}\Pr\bigl(aT_m-\log m-\log\log m-2\log(k-1)\le x\bigr)
=\exp(-e^{-x}). \tag{2}
\]
More strongly, for every fixed \(c\in\mathbb R\) and the *varying* nonhub contact rate \(\gamma_m=\beta(1+c/\log m)\), define
\[
d=\frac{k-1}{k}c,\qquad h(d)=\begin{cases}(1-e^{-d})/d,&d\ne0,\\1,&d=0,\end{cases}\qquad H_k(c)=(k-1)^2h(d).
\]
Then \(H_k(c)>0\) and the nontrivial crossover law is
\[
\boxed{\lim_{m\to\infty}\Pr\bigl(k\beta T_m-\log m-\log\log m-\log H_k(c)\le x\bigr)=\exp(-e^{-x}).} \tag{3}
\]
The extra \(\log\log m\) is a resonance delay, and the crossover occurs on a parameter scale of order \(1/\log m\). The fixed-rate Gumbel and repeated-pole normalization in (1)–(2) are applications of established phase-type extreme-value theory; the network-specific exact constants and the varying-contact-rate limit (3) are the additional result established here.

## Assumptions and scope

Take a graph \(G_{m,k}\) formed by identifying one vertex (the *hub*) of each of \(m\) vertex-disjoint copies of \(K_{k+1}\), with no other edges between copies. There are \(mk+1\) vertices. The hub is infected at time zero and cannot recover. All other vertices are initially susceptible. Each infected–susceptible edge independently transmits at its own exponential rate, hub–leaf edges at \(\beta>0\), edges joining two nonhub vertices of the same clique at \(\gamma\ge0\); transmission occurs at the first contact and infection is permanent. All clocks are independent, including across different cliques. We study the **complete SI infection time**, not the first macroscopic outbreak threshold, an SIR peak time, or a model with recovery.

For (1)–(2), \(k,\beta,\gamma\) stay fixed while integer \(m\to\infty\). For (3), \(k\ge2\), \(\beta>0\), and \(c\in\mathbb R\) stay fixed while \(\gamma_m=\beta(1+c/\log m)\) is used for all \(m\) large enough that \(\gamma_m\ge0\). All logarithms are natural, and \(\operatorname{Exp}(\lambda)\) has mean \(1/\lambda\).

## Proof

**1. Exact petal Markov law.** Fix a clique, with \(j\) infected and \(k-j\) susceptible nonhub vertices. Each susceptible vertex has one infected hub neighbor and exactly \(j\) infected nonhub neighbors. Independent edge transmission therefore gives an instantaneous infection rate \(\beta+j\gamma\) for each susceptible vertex, and total next-infection rate \(\lambda_j=(k-j)(\beta+j\gamma)\). The memorylessness of the independent exponential clocks makes successive count-state holding times independent exponentials of these rates. The infection histories in distinct cliques involve disjoint edge clocks once the hub is initially infected, so their completion times are independent and identically distributed. These facts give the exact expressions above, including when rates coincide. More explicitly, letting \(Q\) be the \(k\)-by-\(k\) upper-bidiagonal transient generator with \(Q_{jj}=-\lambda_j\), \(Q_{j,j+1}=\lambda_j\) for \(j<k-1\), and all other entries zero, the exact all-network distribution is
\[
\Pr(T_m\le t)=\left(1-e_0^\top e^{Qt}{\bf1}\right)^m,\qquad t\ge0.
\]

**2. Slow rates.** As a function of the integer stage \(j\), \(\lambda_j=k\beta+(k\gamma-\beta-\gamma)j-\gamma j^2\) is concave. Its minimum over \(0,\ldots,k-1\) is attained at an endpoint. The endpoint rates are \(\lambda_0=k\beta\) and \(\lambda_{k-1}=\beta+(k-1)\gamma\). If \(\gamma\ne\beta\), the smaller endpoint is the unique minimum (the interior is strictly higher; for \(\gamma=0\) the rates are strictly monotone). If \(\gamma=\beta\), both endpoints equal \(a=k\beta\), and each interior rate is strictly larger since
\[
\lambda_j-a=\beta j(k-j-1)>0,\qquad1\le j\le k-2.
\]

**3. Fixed nonresonant rate.** Write \(D=E_a+U\) with \(E_a\sim\operatorname{Exp}(a)\) independent of the sum \(U\) of all other, strictly faster exponential holding times. Since \(U\) has a moment-generating function finite at some argument above \(a\), the convolution identity gives
\[
\Pr(D>t)\sim e^{-at}\mathbb E[e^{aU}]
=C_{k,\beta,\gamma}e^{-at}.
\]
Taking \(t=(\log m+\log C_{k,\beta,\gamma}+x)/a\), the product \(m\Pr(D>t)\to e^{-x}\). Independence then proves (1) from \((1-p_m)^m\to e^{-\lim mp_m}\).

**4. Exact resonance.** When \(\gamma=\beta\), decompose \(D=E_1+E_2+U\), with \(E_1,E_2\) independent rate-\(a\) exponentials and \(U\) the sum of the strictly faster interior stages. Hence the Erlang-two survival tail and convolution give
\[
\Pr(D>t)\sim a t e^{-at}\mathbb E[e^{aU}].
\]
The prefactor telescopes exactly:
\[
\mathbb E[e^{aU}]=\prod_{j=1}^{k-2}\frac{(k-j)(j+1)}{j(k-j-1)}=(k-1)^2,
\]
with the empty product equal to one for \(k=2\). Taking \(at=\log m+\log\log m+2\log(k-1)+x\) gives \(m\Pr(D>t)\to e^{-x}\), proving (2).

**5. Near-resonant crossover.** Set \(L=\log m\). At \(\gamma_m=\beta(1+c/L)\), the two endpoint rates are \(a=k\beta\) and \(a+\delta_m\), with \(\delta_m=(k-1)\beta c/L\), while all interior rates converge to values strictly above \(a\). Split the petal time as \(D_m=E_a+E_{a+\delta_m}+U_m\), with all components independent. The exact two-stage survival formula is
\[
\Pr(E_a+E_{a+\delta}>t)
=e^{-at}\left[1+a\frac{1-e^{-\delta t}}{\delta}\right]
\quad(\delta\ne0),
\]
with continuous value \(e^{-at}(1+at)\) at \(\delta=0\). For the nearcritical times \(at=L+\log L+O(1)\), one has \(\delta_m t\to d=(k-1)c/k\), whence
\[
\Pr(E_a+E_{a+\delta_m}>t)\sim Lh(d)e^{-at}.
\]
All the interior rates remain greater than \(a+\varepsilon\) for some fixed \(\varepsilon>0\) and sufficiently large \(m\), so \(U_m\) has uniformly bounded exponential moments in a neighborhood above \(a\), and \(\mathbb E[e^{aU_m}]\to(k-1)^2\). Conditioning on \(U_m\), using the two-stage formula on bounded \(U_m\), and controlling its complement by those uniform exponential moments yields the triangular-array tail
\[
\Pr(D_m>t)\sim (k-1)^2h(d)L e^{-at}.
\]
The small term \(\Pr(U_m>t)\) is negligible by the faster exponential tail. With \(at=L+\log L+\log H_k(c)+x\), this implies \(m\Pr(D_m>t)\to e^{-x}\). Petals remain independent for every \(m\), so their maximum converges as in (3). Finally \(h(d)>0\) for all real \(d\) because numerator and denominator have the same sign, with \(h(0)=1\).

## Verification

Run `python3 verify_windmill.py` with Python 3 and its standard library. That program constructs the full labeled-leaf SI continuous-time Markov generator independently of the count reduction and compares exact rational absorption moments through degree four for multiple \(k\) and contact-rate choices. It checks all infection-cut rates, the resonant telescoping coefficient, independent finite-time uniformization probabilities, and the proposed asymptotic centerings for fixed and varying contact rates. It reports 1,733 passed calculations. None of these finite tests is used as a proof of the limit; the symbolic convolution and uniform-moment arguments above establish the infinite assertions.

## Relationship to prior work

Curran-Sebastian, Pellis, Hall and House (2023 preprint; 2024 journal article) study the distribution of times to a macroscopic epidemic threshold and the peak of an outbreak, using branching-process and deterministic approximations. Their SIR outbreak problem does not specify this initial-hub SI clique bouquet or provide its complete-infection law. Ottino-Löffler, Scott and Strogatz (2017) obtain exact takeover and Gumbel results on several networks under a different, discrete-time infection rule. These works motivate quantifying stochastic infection timing on structured networks.

Kang and Serfozo (1999) and Asimit and Jones (2007) establish Gumbel maxima for **fixed** phase-type distributions; the latter explicitly accounts for repeated dominant eigenvalues and logarithmic corrections. Thus the abstract Gumbel limit and the existence of \(\log\log m\) terms at repeated poles are **prior theory**, not original standalone claims here. The present theorem identifies the slow-rate collision generated by two different SI contact mechanisms, gives its exact network-dependent coefficient \((k-1)^2\), and proves an explicit crossover **for a sequence of different phase-type laws** with \(\gamma_m-\beta=\Theta(1/\log m)\). The fixed-distribution theorems do not directly imply this simultaneous varying-rate limit; the preceding proof supplies the necessary uniform control. Standard hypoexponential decomposition itself is not claimed as novel.

## Limitations

The cliques are identical, \(k\) is fixed, the initial infected vertex is the hub, contact clocks are exponential and independent, and infection has no recovery or latent stage. The crossover result fixes \(c\), rather than describing \(c\) growing with \(m\), and does not assert a uniform approximation across all rates. Finite-size convergence may be slow when \(|c|\) is appreciable. No general inhomogeneous-clique, growing-clique-size, or SIR version is proved. Priority relative to all specialist publications has not been independently established; the checked phase-type theorems cover the fixed-rate Gumbel principle but not the specific varying-rate statement established here.

## References

1. J. Curran-Sebastian, L. Pellis, I. Hall, and T. House, *Calculation of Epidemic First Passage and Peak Time Probability Distributions*, arXiv:2301.07058 (first public version January 17, 2023), https://arxiv.org/abs/2301.07058; SIAM/ASA Journal on Uncertainty Quantification 12 (2024), 242–261.
2. E. Ottino-Löffler, M. Scott, and S. H. Strogatz, *Takeover times for a simple model of network infection*, arXiv:1702.00881 (2017), https://arxiv.org/abs/1702.00881.
3. S. Kang and R. F. Serfozo, *Extreme values of phase-type and mixed random variables with parallel-processing examples*, Journal of Applied Probability 36 (1999), 194–210, https://doi.org/10.1239/jap/1032374241.
4. A. V. Asimit and B. Jones, *Extreme behavior of multivariate phase-type distributions*, Insurance: Mathematics and Economics 41 (2007), 223–233, https://openaccess.city.ac.uk/id/eprint/13144/1/Asimit_Jones_2006_revised.pdf.
5. A. Georgiou, *Analysis of the Weighted Clique Heuristic for Community Detection using Cascade Data*, 2022 thesis, https://essay.utwente.nl/fileshare/file/91209/Georgiou_MA_EEMCS.pdf (see the SI complete-graph epidemic and hypoexponential-process discussion).
