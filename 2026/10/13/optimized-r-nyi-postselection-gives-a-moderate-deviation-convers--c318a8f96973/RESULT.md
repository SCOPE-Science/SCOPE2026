# Optimized Rényi postselection gives a moderate-deviation converse window for permutation-symmetric quantum codes
## Finding
Let \(\mathcal N:A\to B\) be a finite-dimensional quantum channel with \(d=\dim A\ge2\). Define
\[
q_n^{{\mathrm{{sym}}}}(\mathcal N)=\frac1n\max_{{\rho_{{A^n}}\ \mathrm{{permutation\ invariant}}}} I_c(\mathcal N^{{\otimes n}},\rho_{{A^n}}),
\]
\[
g_{{n,d}}=\binom{{n+d^2-1}}{{d^2-1}},\qquad L_{{n,d}}=\log_2 g_{{n,d}}.
\]
There are finite constants \(a_{{\mathcal N}},c_{{\mathcal N}}\ge0\), depending only on \(\mathcal N\), such that for every integer \(n\ge1\) and every \(0<t\le1/2\),
\[
q_n^{{\mathrm{{sym}}}}(\mathcal N)
\le Q^{{(1)}}(\mathcal N)+a_{{\mathcal N}}t+c_{{\mathcal N}}t^2
+\frac{{1+t}}{{nt}}L_{{n,d}}.
\tag{{1}}
\]
Hence, if \(L_{{n,d}}\le n/4\), choosing \(t=\sqrt{{L_{{n,d}}/n}}\) yields
\[
q_n^{{\mathrm{{sym}}}}(\mathcal N)-Q^{{(1)}}(\mathcal N)
\le (a_{{\mathcal N}}+1)\sqrt{{\frac{{L_{{n,d}}}}{{n}}}}
+(c_{{\mathcal N}}+1)\frac{{L_{{n,d}}}}{{n}}.
\tag{{2}}
\]
Because \(L_{{n,d}}=(d^2-1)\log_2 n+O_d(1)\), this is
\[
q_n^{{\mathrm{{sym}}}}(\mathcal N)-Q^{{(1)}}(\mathcal N)
=O_{{\mathcal N,d}}\!\left(\sqrt{{\frac{{\log n}}{{n}}}}\right).
\tag{{3}}
\]

The same optimization gives a shrinking-gap strong converse. Consider the pure-source entanglement-generation codes of arXiv:2610.02176v1, with a permutation-invariant channel input, rate
\[
r=Q^{{(1)}}(\mathcal N)+\Delta,
\]
and squared target fidelity \(f\). For every \(0<t\le1/2\),
\[
f\le \min\left\{{1,\;2^{{L_{{n,d}}-\frac{{nt}}{{1+t}}(\Delta-a_{{\mathcal N}}t-c_{{\mathcal N}}t^2)}}\right\}}.
\tag{{4}}
\]
Set \(K_{{\mathcal N}}=a_{{\mathcal N}}+c_{{\mathcal N}}+1\). For \(0<\Delta\le K_{{\mathcal N}}\), taking \(t=\Delta/(2K_{{\mathcal N}})\) gives
\[
f\le \min\left\{{1,\;g_{{n,d}}2^{{-n\Delta^2/(6K_{{\mathcal N}})}}\right\}}.
\tag{{5}}
\]
Therefore every sequence \(\Delta_n\downarrow0\) satisfying
\[
\frac{{\Delta_n}}{{\sqrt{{\log n/n}}}}\longrightarrow\infty
\]
has \(f_n\to0\).

## Assumptions and scope
The channel is finite dimensional and \(d\ge2\). The input to all \(n\) channel uses is invariant under every permutation. The code statement applies to the pure-source entanglement-generation class used in arXiv:2610.02176v1, including entanglement transmission with an isometric encoder and permutation-invariant channel input. It does not cover arbitrary mixed encoders whose decompositions may destroy the imposed symmetry.

All logarithms are base two. The constants \(a_{{\mathcal N}}\) and \(c_{{\mathcal N}}\) are any nonnegative uniform constants for which, for \(0<t\le1/2\),
\[
Q^\downarrow_{{1+t}}(\mathcal N)
\le Q^{{(1)}}(\mathcal N)+a_{{\mathcal N}}t+c_{{\mathcal N}}t^2.
\tag{{6}}
\]
The uniform variance and Taylor-remainder argument in arXiv:2610.02176v1 proves that such constants exist. In the notation of that proof one may take the linear coefficient from the uniform relative-entropy-variance bound and enlarge the uniform remainder constant to be nonnegative.

## Proof
For a permutation-invariant input, the exact postselection factor in arXiv:2610.02176v1 is \(g_{{n,d}}\). Its equation (33), whose proof uses the symmetric purification and Lemma 15, gives for every \(\alpha>1\)
\[
-\widetilde H^\uparrow_\alpha(R^n\mid B^n)
\le nQ^\downarrow_\alpha(\mathcal N)
+\frac{{\alpha}}{{\alpha-1}}L_{{n,d}}.
\tag{{7}}
\]
Put \(\alpha=1+t\), with \(0<t\le1/2\). Equations (20)--(23) of the same source establish a uniform second-order expansion at \(\alpha=1\), giving (6). Since
\[
I_c(\mathcal N^{{\otimes n}},\rho_{{A^n}})
=-S(R^n\mid B^n)
\le-\widetilde H^\uparrow_{{1+t}}(R^n\mid B^n),
\]
combining (6) and (7), maximizing over permutation-invariant inputs, and dividing by \(n\) proves (1). Substitution of \(t=\sqrt{{L_{{n,d}}/n}}\) gives (2) exactly, and the fixed-\(d\) asymptotic for the binomial coefficient gives (3).

For the code statement, equation (31) of arXiv:2610.02176v1 gives, with \(f\) the squared target fidelity,
\[
\log_2 M
\le -\widetilde H^\uparrow_{{1+t}}(R\mid B^n)
-\frac{{1+t}}t\log_2 f.
\tag{{8}}
\]
Write \(r=n^{{-1}}\log_2 M=Q^{{(1)}}(\mathcal N)+\Delta\). Combining (6)--(8) and rearranging yields
\[
-\log_2 f
\ge \frac{{nt}}{{1+t}}\bigl(\Delta-a_{{\mathcal N}}t-c_{{\mathcal N}}t^2\bigr)-L_{{n,d}},
\]
which is (4).

For (5), let \(K_{{\mathcal N}}=a_{{\mathcal N}}+c_{{\mathcal N}}+1\) and \(t=\Delta/(2K_{{\mathcal N}})\). The hypothesis \(0<\Delta\le K_{{\mathcal N}}\) ensures \(0<t\le1/2\). Also
\[
a_{{\mathcal N}}t+c_{{\mathcal N}}t^2
\le(a_{{\mathcal N}}+c_{{\mathcal N}})t
<\frac\Delta2,
\]
and
\[
\frac{t}{1+t}=\frac{\Delta}{2K_{{\mathcal N}}+\Delta}
\ge\frac{\Delta}{3K_{{\mathcal N}}}.
\]
Thus
\[
\frac{{nt}}{{1+t}}\bigl(\Delta-a_{{\mathcal N}}t-c_{{\mathcal N}}t^2\bigr)
\ge\frac{{n\Delta^2}}{{6K_{{\mathcal N}}}},
\]
which proves (5). Since \(L_{{n,d}}=O_d(\log n)\), the stated shrinking-gap condition forces the exponent to diverge.

## Verification
The proof is analytic and applies to every finite-dimensional channel satisfying the stated symmetry restriction. The standalone script `artifacts/verify.py` checks the algebraic substitutions and the elementary inequalities used to pass from (1) and (4) to (2) and (5) over a deterministic grid of admissible parameters. It does not attempt to numerically certify the source's operator inequalities; those are used in their stated proven form.

## Relationship to prior work
Baghali Khanian, Leung, and Smith, arXiv:2610.02176v1, prove the exact postselection inequality (7), the uniform Rényi-order expansion (6), an \(O(\log n/\sqrt n)\) coherent-information correction, and a fixed-rate strong converse. Their proof fixes \(\alpha=1+n^{{-1/2}}\). Retaining \(t=\alpha-1\) as a free parameter and balancing its Taylor cost against the exact postselection factor gives the sharper scale in (2)--(5). The source does not state a shrinking-gap converse or the \(O(\sqrt{{\log n/n}})\) coherent-information rate.

Kossmann and Zeiss, arXiv:2607.23689, obtain refined de Finetti convergence for fixed-point hierarchies, but their extension/separability estimates concern a different approximation problem and do not imply (1)--(5). Chubb, Tan, and Tomamichel, arXiv:1701.03114, study moderate deviations for classical communication over classical-quantum and image-additive channels; their result is operationally and mathematically distinct from the permutation-symmetric quantum-communication code class here.

## Limitations
No optimality of the \(\sqrt{{\log n/n}}\) window or the constant \(6K_{{\mathcal N}}\) is claimed. The bound is a converse under full permutation invariance, not an achievability theorem and not a statement about unrestricted quantum capacity. The channel-dependent constants are finite but are not evaluated here for specific channels. The result does not assert that permutation-symmetric codes attain \(Q^{{(1)}}(\mathcal N)\).

## References
1. Z. Baghali Khanian, D. Leung, and G. Smith, “From Permutation Symmetry to Communication Bounds and Additivity,” arXiv:2610.02176v1, 1 October 2026.
2. G. Kossmann and J. A. Zeiss, “Fixed points in de Finetti hierarchies,” arXiv:2607.23689, 26 July 2026.
3. C. T. Chubb, V. Y. F. Tan, and M. Tomamichel, “Moderate deviation analysis for classical communication over quantum channels,” Communications in Mathematical Physics 355 (2017), arXiv:1701.03114.
