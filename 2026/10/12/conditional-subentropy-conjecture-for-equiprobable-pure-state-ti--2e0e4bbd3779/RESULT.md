# Conditional subentropy conjecture for equiprobable pure-state tight frames
## Finding
Let \(n\ge d\ge1\), and let \(\{|\psi_x\rangle}\}_{x=1}^n\subset\mathbb C^d\) be unit vectors satisfying the tight-frame identity
\[
\sum_{x=1}^n |\psi_x\rangle\langle\psi_x|=\frac nd I_d.
\]
For the equiprobable classical--quantum state
\[
\rho_{XB}=\frac1n\sum_{x=1}^n |x\rangle\langle x|\otimes|\psi_x\rangle\langle\psi_x|,
\]
the optimal guessing probability, min-conditional entropy, and conditional subentropy are
\[
p_{\mathrm{guess}}(X|B)=\frac dn,
\qquad
H_{\min}(X|B)=\log\frac nd,
\]
and
\[
Q(X|B)=\log\frac nd-(H_n-H_d),
\qquad
H_k=\sum_{j=1}^k\frac1j.
\]
Therefore
\[
Q(X|B)\le H_{\min}(X|B)=-\log p_{\mathrm{guess}}(X|B),
\]
with exact gap \(H_n-H_d\). Equality holds exactly for \(n=d\); then the unit-norm tight frame is an orthonormal basis. Every overcomplete case \(n>d\) is strict.

This proves Datta--Dorlas--Jozsa--Benatti Conjecture 2 on the full class of equiprobable pure-state unit-norm tight-frame ensembles, equivalently equal-weight complex projective one-designs. No equiangularity or group covariance is assumed.

## Assumptions and scope
All Hilbert spaces are finite dimensional and all logarithms are natural. The classical labels \(|x\rangle\) are orthonormal. Each signal \(|\psi_x\rangle\) is a unit vector in \(\mathbb C^d\), and \(n\ge d\). Conditional subentropy is the quantity introduced in arXiv:1310.1312,
\[
Q(X|B)=Q(\rho_{XB})-Q(\rho_B).
\]
The claim concerns equiprobable pure-state ensembles whose average state is maximally mixed. It does not address nonuniform priors, mixed signal states, or general pure-state ensembles.

## Proof
First compute the average state:
\[
\rho_B=\frac1n\sum_{x=1}^n|\psi_x\rangle\langle\psi_x|=\frac1d I_d.
\]
For any POVM \(\{E_x}\}_{x=1}^n\), positivity and \(|\psi_x\rangle\langle\psi_x|\preceq I_d\) give
\[
\frac1n\sum_x\operatorname{Tr}\!\left(E_x|\psi_x\rangle\langle\psi_x|\right)
\le \frac1n\sum_x\operatorname{Tr}(E_x)=\frac dn.
\]
The operators
\[
E_x=\frac dn|\psi_x\rangle\langle\psi_x|
\]
form a POVM by the tight-frame identity and attain the upper bound. Hence
\[
p_{\mathrm{guess}}(X|B)=\frac dn,
\qquad
H_{\min}(X|B)=\log\frac nd.
\]

It remains to compute the two subentropies. We use the following uniform-rank lemma. If a density operator has \(r\) nonzero eigenvalues, all equal to \(1/r\), then
\[
Q=\log r-H_r+1,
\qquad
H_r=\sum_{j=1}^r\frac1j,
\]
independently of any additional zero eigenvalues in the ambient space.

To prove the lemma, use the simplex integral representation from arXiv:1310.1312. In ambient dimension \(N\), with normalized uniform measure on the probability simplex,
\[
Q(\rho)=N\,\mathbb E\!\left[-(\lambda\cdot X)\log(\lambda\cdot X)\right]-(H_N-1).
\]
For spectrum \((1/r,\ldots,1/r,0,\ldots,0)\), write \(S=X_1+\cdots+X_r\). If \(r<N\), then \(S\) has the beta distribution with parameters \(r\) and \(N-r\), and
\[
\mathbb E S=\frac rN,
\qquad
\mathbb E(S\log S)=\frac rN(H_r-H_N).
\]
Therefore
\[
N\,\mathbb E\!\left[-\frac Sr\log\frac Sr\right]
=H_N-H_r+\log r,
\]
and subtraction of \(H_N-1\) gives \(Q=\log r-H_r+1\). For \(r=N\), the same formula follows directly from the maximally mixed value \(Q(I_N/N)=\log N-(H_N-1)\).

Now \(\rho_{XB}\) is block diagonal with exactly \(n\) nonzero eigenvalues, each \(1/n\), while \(\rho_B=I_d/d\). Thus
\[
Q(\rho_{XB})=\log n-H_n+1,
\qquad
Q(\rho_B)=\log d-H_d+1,
\]
and hence
\[
Q(X|B)=\log\frac nd-(H_n-H_d).
\]
Subtracting from \(H_{\min}(X|B)=\log(n/d)\) yields
\[
H_{\min}(X|B)-Q(X|B)=H_n-H_d\ge0.
\]
The gap vanishes exactly when \(n=d\). A square unit-norm tight frame has synthesis matrix \(F\) satisfying \(FF^*=I_d\), hence \(F\) is unitary and its columns form an orthonormal basis.

## Verification
The accompanying `verify.py` reconstructs Fourier tight-frame examples for a grid of \((n,d)\), checks the frame operator and the self-referential POVM numerically, verifies the success probability \(d/n\), and checks the harmonic-number gap exactly as a rational number. Running it prints `VERIFY_OK`.

The infinite-dimensional quantifiers in the theorem are discharged by the analytic proof above; the checker is a reproducibility aid, not an exhaustive proof by enumeration.

## Relationship to prior work
Datta, Dorlas, Jozsa, and Benatti introduced conditional subentropy and conjectured
\[
Q(X|B)\le H_{\min}(X|B)=-\log p_{\mathrm{guess}}(X|B)
\]
for classical--quantum states. They proved the pure-state case with two classical labels and reported numerical evidence for three labels. Their paper also supplies the simplex integral representation of subentropy used above.

The tight-frame/POVM connection is classical in quantum detection theory. Eldar and Forney relate normalized tight frames to rank-one quantum measurements. More recently, Farokhi and Xiao explicitly prove that an equiprobable unit-norm tight-frame ensemble has optimal minimum-error discrimination probability \(d/n\). That discrimination statement is therefore prior work; the new contribution here is the exact conditional-subentropy evaluation and its implication for the 2013 conditional-subentropy conjecture over all \(n\ge d\).

Targeted searches for the conjecture together with `tight frame`, `projective 1-design`, the exact ratio \(d/n\), and the harmonic gap found no source stating the displayed conditional-subentropy formula or this all-dimensional conjecture sector. This is evidence against direct coverage, not a proof that differently indexed literature cannot contain an equivalent result.

## Limitations
The result requires equal priors, pure signals, and a maximally mixed ensemble average. It does not prove the conjecture for arbitrary classical--quantum states. The recent tight-frame discrimination theorem covers one ingredient of the proof, so originality rests on the exact subentropy calculation and the resulting conjecture sector, not on the value \(p_{\mathrm{guess}}=d/n\) by itself. A residual literature risk remains that an equivalent conditional-subentropy statement is phrased under projective-design or frame terminology not retrieved by the searches performed.

## References
1. N. Datta, T. Dorlas, R. Jozsa, F. Benatti, *Properties of subentropy*, arXiv:1310.1312, DOI 10.1063/1.4882935. First public version: 2013-10-04.
2. Y. C. Eldar, G. D. Forney Jr., *Optimal Tight Frames and Quantum Measurement*, arXiv:quant-ph/0106070.
3. F. Farokhi, S. Xiao, *An Information-Theoretic Principle for Optimal Quantum Encoding: Tight Frames and Equiangular Ensembles*, arXiv:2607.01564.
