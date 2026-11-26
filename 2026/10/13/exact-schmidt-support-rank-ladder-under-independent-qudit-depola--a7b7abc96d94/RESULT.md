# Exact Schmidt-support rank ladder under independent qudit depolarization

## Finding

Let \(d\ge 3\) be an integer. A controlled shift sends \(|j\rangle|0\rangle\) to \(|jj\rangle\); a uniform superposition on \(k\) computational basis labels thus produces \(|\Phi_{d,k}\rangle=k^{-1/2}\sum_{j=0}^{k-1}|jj\rangle\), up to relabelling. Subject the two outputs independently to the channels \(\mathcal D_p(X)=(1-p)X+(p/d)\operatorname{Tr}(X)I_d\) and \(\mathcal D_q\) defined likewise, with \(p,q\in[0,1]\). Write \(\rho_{d,k;p,q}\) for the resulting density operator, \(\mathcal N_k=(\|\rho_{d,k;p,q}^{T_B}\|_1-1)/2\), and
\[
\Delta=d^2(1-p)(1-q)-d[p(1-q)+q(1-p)],\qquad \Pi=pq.
\]
For \(1\le k\le d\) the exact negativity is
\[
\mathcal N_k=\frac{k-1}{2d^2}[\Delta-k\Pi]_+,\qquad [z]_+=\max(0,z).
\]

The optimization here is over the uniform-on-support inputs, not over arbitrary Schmidt spectra. If \(\Pi>0\) and \(\Delta\le 2\Pi\), all ranks tie at zero. If \(\Pi>0\) and \(\Delta>2\Pi\), the maximum is positive. Its rank is unique except on \(\Delta=2k\Pi\), \(2\le k<d\), where exactly ranks \(k,k+1\) tie. In the positive region the maximizing rank increases as \(\Delta/\Pi\) increases past the successive thresholds. If \(\Pi=0\) and \(\Delta>0\), rank \(d\) is uniquely optimal; if \(\Pi=0\) and \(\Delta\le0\), every rank ties at zero. **Rank one is never uniquely optimal:** it has zero negativity for every noise pair.

For symmetric noise \(p=q=t\), each of the ranks **\(2,3,\ldots,d\)** is the unique maximizer on a nonempty open interval of \(t\in(0,1)\). As \(t\) increases from zero, the maximizing ranks visit \(d,d-1,\ldots,2\), with the switch between \(k+1\) and \(k\) at
\[
t_k=\frac{d}{d+1+\sqrt{2k+1}},\qquad 2\le k<d.
\]
The family is entirely PPT from \(t_{\mathrm{death}}=d/(d+1+\sqrt3)\) onward. The full-support state becomes PPT already at \(t_{\mathrm{full}}=1-1/\sqrt{d+1}\). For example, at \(d=3\), \(p=q=1/2\), \(\mathcal N_3=0\) but \(\mathcal N_2=1/72\). The all-input entanglement-annihilation endpoint of Lami and Huber is prior work; the contribution here is the magnitude comparison and rank ladder in the stated family.

## Assumptions and scope

The input is pure with equal magnitudes on its support, the ancilla begins in \(|0\rangle\), and the channels act independently after the gate. Local unitary covariance and invariance of the partial-transpose trace norm make all choices of basis labels (and local phases) equivalent at fixed \(k\). The parameters are probabilities in the trace-to-maximally-mixed convention. The objective is negativity; logarithmic negativity gives the same optimizing rank by monotonicity. No optimization over nonuniform spectra, correlated noise, mixed inputs or other entanglement measures is asserted. Zero negativity means PPT, not in general separability.

## Proof

Set \(P_k=\sum_{j<k}|j\rangle\langle j|\) and \(\rho_0=|\Phi_{d,k}\rangle\langle\Phi_{d,k}|\). Its reductions are \(P_k/k\), so expansion of the product channel gives
\[
\rho_{d,k;p,q}=(1-p)(1-q)\rho_0+\frac{p(1-q)}{dk}I_d\otimes P_k+
\frac{(1-p)q}{dk}P_k\otimes I_d+\frac{pq}{d^2}I_d\otimes I_d.
\]
The off-diagonal terms after the second-system transpose couple exactly \(|ij\rangle,|ji\rangle\) for \(0\le i<j<k\). Each such pair has diagonal entries \(h_k=[p(1-q)+(1-p)q]/(dk)+pq/d^2\) and off-diagonal entries \(g_k=(1-p)(1-q)/k\). Thus its eigenvalues are \(h_k\pm g_k\); other eigenvalues are nonnegative diagonal entries. The possible negative mass in a pair is \([g_k-h_k]_+=[\Delta-k\Pi]_+/(kd^2)\). Summing over \(k(k-1)/2\) pairs gives the negativity formula, including \(k=1\) with no pairs.

Let \(f(k)=(k-1)(\Delta-k\Pi)\), so the scores before division by \(2d^2\) are \([f(k)]_+\). For \(\Pi>0\) and \(\Delta\le2\Pi\) no score is positive; otherwise \(f(2)>0\) and truncation leaves the maximizing set unchanged. The successive differences are \(f(k+1)-f(k)=\Delta-2k\Pi\), strictly decreasing with \(k\). This gives the claimed ordering and the exact two-rank ties, and excludes a positive rank-one tie because \(f(1)=0\). For \(\Pi=0\), the score is \((k-1)[\Delta]_+\), directly yielding the two boundary cases.

For \(0<t<1\) put \(x=d(1-t)/t\); then \(\Delta/\Pi=x^2-2x\). In the positive region \(x>1+\sqrt3\), so the ratio is strictly decreasing as \(t\) increases. The equation \(\Delta/\Pi=2k\) has the unique nonnegative solution \(x=1+\sqrt{2k+1}\), giving the switches in order and a nonempty strict interval for every \(k\ge2\). The last positive rank is 2, so its death is the equality \(\Delta/\Pi=2\). For full support, the equality \(\Delta=d\Pi\) reduces to \((d+1)(1-t)^2=1\), giving \(t_{\mathrm{full}}\). At the qutrit example \((\Delta,\Pi)=(3/4,1/4)\), giving the stated values exactly.

## Verification

The block spectrum and finite differences prove the claims on the whole domain. The accompanying `artifacts/verify.py` constructs the full channel output and computes its partial-transpose spectrum in representative dimensions and noise settings. It compares the formula with numerical spectra, checks ties and strict intervals for entangled support ranks, and checks the qutrit example with rational arithmetic. `artifacts/requirements.txt` specifies NumPy. These checks are corroborative, not a proof outside their test cases.

## Relationship to prior work and limitations

Ali et al., arXiv:2606.16695v1, §V.B, Eqs. (43)–(49), treat the global depolarizing channel explicitly distinguished from a product of local channels. Their negativity formula for that channel is not the formula for independent local depolarization above. Lami and Huber, *Bipartite depolarizing channels*, arXiv:1603.02158v1, Theorem 7 and Corollary 8, characterize all-input entanglement annihilation under local depolarization; the rank-two witness detects the all-input boundary and the symmetric endpoint in their visibility convention \(1-t\) is precisely \(t_{\mathrm{death}}\). Neither the all-input boundary nor sharpness at that boundary is claimed as new. The intermediate comparisons above maximize the magnitude of negativity below that boundary in the specified family. Earlier two-qubit robustness results (e.g. Filippov, Frizen and Kolobova, arXiv:1708.08208) address a different dimension or optimization; they do not yield the \(d\ge3\) ladder. No global optimum over arbitrary input spectra is claimed.
