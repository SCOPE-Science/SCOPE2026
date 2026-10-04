# Thermal purifications force a \(1.295220\) lower barrier for balanced-loss information variance
## Finding
Let \(C_{\mathrm{bal}}\) denote the best universal coefficient in the balanced pure-loss relative-entropy-variance estimate over the finite-photon-support pure inputs of Wilde's Lemma 2. Thus \(C_{\mathrm{bal}}\) is the infimum of all \(C\) for which
\[
V(\omega_{RB^n}\|I_R\otimes\sigma_{B^n})\le Cn
\]
holds for every number of modes \(n\), every finite-dimensional reference, and every pure input with finite total-photon-number support. Wilde proved \(C_{\mathrm{bal}}\le4\). We prove the complementary lower barrier
\[
C_{\mathrm{bal}}\ge C_*=2x_*(2-x_*)=1.295220475783829\ldots,
\]
where \(x_*\in(1,2)\) is the unique solution of \((2-x)e^x=2\).

Equivalently, no uniform estimate of the same form can have coefficient smaller than \(1.295220475783829\ldots\). The witnesses are finite truncations of a natural geometric, or thermal, purification; tensor powers make the lower barrier extensive in the number of modes.

## Assumptions and scope
The channel is the balanced pure-loss bosonic channel, with transmissivity \(1/2\), and logarithms are natural. For one mode fix \(q\in(0,1)\) and an integer cutoff \(L\ge0\). Define
\[
p_m^{(L)}=\frac{(1-q)q^m}{1-q^{L+1}},\qquad 0\le m\le L,
\]
and the finite-support purification
\[
|\phi_{q,L}\rangle=\sum_{m=0}^L\sqrt{p_m^{(L)}}\,|m\rangle_R|m\rangle_A.
\]
The reference has dimension \(L+1\), and the input has photon-number support at most \(L\), so this family lies exactly inside the finite-support domain of the source variance lemma.

For \(n\) modes we use the tensor power \(|\phi_{q,L}\rangle^{\otimes n}\). Its total photon number is at most \(nL\), hence it also remains in that domain.

## Proof
After a balanced beam splitter, the one-mode global state is
\[
|\psi_{q,L}\rangle
=\sum_{m=0}^L\sum_{k=0}^m
\sqrt{p_m^{(L)}\binom{m}{k}2^{-m}}\,
|m\rangle_R|k\rangle_B|m-k\rangle_E.
\]
The receiver and environment marginals coincide and are diagonal in photon number. Write
\[
\sigma_B^{(L)}=\sum_{j=0}^L s_j^{(L)}|j\rangle\langle j|,
\qquad
s_j^{(L)}=\sum_{m=j}^L p_m^{(L)}\binom{m}{j}2^{-m}.
\]
Wilde's balanced-output identity gives zero relative entropy and expresses the variance as the squared norm of \(Y|\psi\rangle\), with \(Y=\ln\sigma_B-\ln\sigma_E\). Here that identity is completely explicit, because both marginals are diagonal. Hence
\[
V_L(q)=\sum_{m=0}^L p_m^{(L)}\sum_{k=0}^m
\binom{m}{k}2^{-m}
\left(\ln s_k^{(L)}-\ln s_{m-k}^{(L)}\right)^2.
\]

For every fixed \(j\), as \(L\to\infty\),
\[
s_j^{(L)}\longrightarrow
(1-q)\sum_{m=j}^\infty q^m\binom{m}{j}2^{-m}
=(1-r)r^j,
\qquad
r=\frac{q}{2-q}.
\]
Therefore, for every fixed pair \((m,k)\), the logarithmic difference tends to \((2k-m)\ln r\). Extend the finite-cutoff summands by zero outside \(m\le L\). They are nonnegative, so Fatou's lemma yields
\[
\liminf_{L\to\infty}V_L(q)
\ge
\sum_{m\ge0}(1-q)q^m\sum_{k=0}^m\binom{m}{k}2^{-m}
(2k-m)^2(\ln r)^2.
\]
Conditional on \(m\), the random variable \(k\) is binomial with parameters \(m\) and \(1/2\), and thus
\[
\mathbb E[(2k-m)^2\mid m]=m.
\]
The geometric distribution has mean \(q/(1-q)\). Consequently
\[
\liminf_{L\to\infty}V_L(q)
\ge C(q):=\frac{q}{1-q}\left[\ln\!\left(\frac{q}{2-q}\right)\right]^2.
\]
In particular, for every \(\varepsilon>0\) there is a finite \(L\) with \(V_L(q)>C(q)-\varepsilon\).

To optimize this certified lower bound, set \(r=e^{-x}\), so that \(q=2e^{-x}/(1+e^{-x})\). Then
\[
C(q)=\frac{2x^2}{e^x-1}.
\]
The derivative vanishes exactly when
\[
(2-x)e^x=2.
\]
Besides the boundary root at \(x=0\), the function \((2-x)e^x-2\) is positive at \(x=1\), negative at \(x=2\), and strictly decreasing for \(x>1\). Thus there is a unique interior maximizer \(x_*\in(1,2)\). At that root,
\[
e^{x_*}-1=\frac{x_*}{2-x_*},
\]
so
\[
C_*=\frac{2x_*^2}{e^{x_*}-1}=2x_*(2-x_*)=1.295220475783829\ldots.
\]

Finally, relative-entropy variance is additive for tensor products when each factor has zero relative entropy: the tensor-product log-likelihood is the sum of the factor log-likelihoods, and the cross terms vanish because each factor has mean zero. Hence the \(n\)-fold tensor power of a one-mode cutoff witness has variance \(nV_L(q)\). For every \(\varepsilon>0\), choosing \(q=q_*\) and then a sufficiently large finite \(L\) gives admissible \(n\)-mode witnesses with
\[
\frac1nV(\omega_{RB^n}\|I_R\otimes\sigma_{B^n})>C_*-\varepsilon.
\]
This proves \(C_{\mathrm{bal}}\ge C_*\).

## Verification
The bundled checker independently solves the scalar maximization equation, evaluates the exact finite-cutoff sum above, and verifies rapid convergence of the cutoff values to the analytic constant. At the maximizing parameter it obtains \(x_*=1.593624260040040\ldots\), \(q_*=0.337749199521702\ldots\), and \(C_*=1.295220475783830\ldots\). The \(L=20\) finite-cutoff value differs from \(C_*\) by less than \(4\times10^{-11}\).

The finite computation is corroborative. The all-cutoff lower-barrier statement follows from the explicit variance identity, pointwise geometric limit, Fatou's lemma, elementary binomial variance, and tensor-product additivity.

## Relationship to prior work
Wilde's 2026 strong-converse paper proves the cutoff-independent upper estimate \(V\le4n\) for exactly this balanced-loss quantity and explicitly identifies improvement of its constant as an open finite-blocklength question. The present result supplies a rigorous lower obstruction: any improved universal coefficient must still be at least \(C_*\).

Wilde, Renes, and Guha's 2014 second-order paper computes the entropy variance of a thermal output for energy-constrained classical communication. That quantity is different from the reference-output relative-entropy variance in the 2026 balanced-loss lemma. Its thermal formula motivates comparison with geometric photon statistics but does not imply the optimized finite-support lower barrier proved here.

## Limitations
The result does not determine the exact universal coefficient. It establishes only
\[
1.295220475783829\ldots\le C_{\mathrm{bal}}\le4.
\]
The lower endpoint is the exact optimum of the limiting truncated-geometric family described above, not a proof of global optimality among all admissible inputs. The infinite geometric purification itself is used only as a limiting device; every actual witness invoked in the theorem has finite photon-number support.

No dispersion formula or sharp second-order coding theorem is claimed.

## References
[1] M. M. Wilde, “Strong converse for the quantum capacity of the pure-loss bosonic channel,” arXiv:2609.16608v1, 2026.

[2] M. M. Wilde, J. M. Renes, and S. Guha, “Second-order coding rates for pure-loss bosonic channels,” arXiv:1408.5328v1, 2014.
