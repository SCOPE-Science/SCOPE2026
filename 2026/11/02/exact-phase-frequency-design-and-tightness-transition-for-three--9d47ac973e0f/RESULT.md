# Exact phase–frequency design and tightness transition for three-tap cyclic Gabor frames

## Finding

Fix an integer \(N\ge5\) and positive numbers \(u,v,w\) with \(u^2+v^2+w^2=1\). Among all windows \(g=(a,b,c,0,\ldots,0)\in\mathbb C^N\) with \((|a|,|b|,|c|)=(u,v,w)\), and all unordered pairs of distinct modulation indices, the **sharp minimum of the frame potential** of the full-translation two-channel cyclic Gabor system is
\[
\Phi_{\min}=4N+8N\min_{1\le d\le\lfloor N/2\rfloor}
\bigl[v^2(u-w)^2t_d+u^2w^2(2t_d-1)^2\bigr],
\qquad t_d=\cos^2(\pi d/N).
\]
Set \(B=u^2w^2>0\), \(A=v^2(u-w)^2\), and
\[
\tau=\max\{0,(4B-A)/(8B)\}\in[0,1/2].
\]
**All minimizing gaps** are exactly the integers \(d\in\{1,\ldots,\lfloor N/2\rfloor\}\) for which \(t_d\) is nearest to \(\tau\). For each such gap with \(t_d>0\), **all minimizing phases** satisfy
\[
\arg(ac/b^2)\equiv\pi\pmod{2\pi};
\]
if \(t_d=0\) (only the antipodal gap in even order), every coefficient phase is optimal. Arbitrary translations of the two modulation labels do not change the answer. Every minimizing system is a genuine frame.

The sharp potential excess admits the **exact nonnegative two-term design deficit**
\[
\Phi-\Phi_{\min}=8N\Bigl[4uv^2w\,t_d\cos^2\!\bigl(\tfrac12\arg(ac/b^2)\bigr)
+F(t_d)-\min_e F(t_e)\Bigr],
\quad F(t)=At+B(2t-1)^2.
\]
For the symmetric magnitude family \(u=w\), this specializes to
\[
\Phi-4N=32N\left[u^2v^2\,t_d\cos^2\!\bigl(\tfrac12\arg(ac/b^2)\bigr)
+u^4\bigl(t_d-\tfrac12\bigr)^2\right].
\]
Consequently, within the prescribed strictly positive magnitude class, a tight two-channel full-translation Gabor frame exists **if and only if** \(u=w\) and \(4\mid N\); its complete design locus consists of quarter-cycle gaps \(d=N/4\) and the phase relation \(ac/b^2<0\).

As a concrete distinction at identical magnitudes, if \(4\mid N\), the positive boxcar window \((1,1,1)/\sqrt3\) has best potential \(44N/9\), whereas \((1,1,-1)/\sqrt3\) with a quarter-cycle modulation gap gives a tight frame of potential \(4N\). For positive symmetric windows \((1,\beta,1)/\sqrt{2+\beta^2}\) on an even cycle, the antipodal modulation gap is optimal precisely when \(\beta\ge\cos(\pi/N)\), with a tie at equality. These are exact finite-size design thresholds, not large-order heuristics.

## Assumptions and scope

The Hilbert space is \(\mathbb C^N\) with its unnormalized Euclidean inner product. Put \(\zeta=e^{2\pi i/N}\); define \((T_kg)[j]=g[j-k]\) and \((M_\ell g)[j]=\zeta^{\ell j}g[j]\), with all coordinates read modulo \(N\). The system comprises exactly the \(2N\) unit vectors
\[
\mathcal G(g,L)=\{M_\ell T_kg:\ell\in L,\ k\in\mathbb Z_N\},
\qquad L=\{\ell_0,\ell_1\},\quad\ell_0\ne\ell_1.
\]
Its frame operator is \(S=\sum_{h\in\mathcal G}hh^*\). Its Benedetto–Fickus frame potential is \(\Phi=\sum_{h,h'\in\mathcal G}|\langle h,h'\rangle|^2=\operatorname{tr}(S^2)\). Thus \(\operatorname{tr}S=2N\), \(\Phi\ge4N\), and equality is equivalent to \(S=2I\). Gaps are identified up to sign, so representatives \(d\) run from \(1\) to \(\lfloor N/2\rfloor\). All three magnitudes are strictly positive; the vanishing-tap boundary is not covered.

## Proof

**1. Exact Fourier spectrum and potential.** Write \(P(z)=a+bz+cz^2\). The full-translation diagonalization (a classical finite Gabor identity) gives the eigenvalue multiset
\[
\{\lambda_j:0\le j<N\}=\{\,|P(\zeta^{j-\ell_0})|^2+|P(\zeta^{j-\ell_1})|^2:0\le j<N\,\}.
\]
This can also be checked directly by Fourier-transforming all cyclic translates and using character orthogonality. The squared modulus \(|P(z)|^2\) on \(|z|=1\) has constant coefficient one, lag-one coefficient of magnitude \(|C_1|\), and lag-two coefficient of magnitude \(|C_2|\), where
\[
C_1=a\overline b+b\overline c,\qquad C_2=a\overline c.
\]
For \(N\ge5\), the five Fourier characters of degrees \(0,\pm1,\pm2\) are distinct. Orthogonality, together with \(|1+\zeta^d|^2=4t_d\) and \(|1+\zeta^{2d}|^2=4(2t_d-1)^2\), yields the **exact** identity
\[
\Phi-4N=8N\bigl(|C_1|^2t_d+|C_2|^2(2t_d-1)^2\bigr). \tag{1}
\]
There is no asymptotic approximation and no hidden normalization factor.

**2. Phase minimization.** Since \(a,b,c\ne0\), let \(\phi=\arg(ac/b^2)\pmod{2\pi}\). Elementary expansion gives
\[
|C_1|^2=v^2(u-w)^2+4uv^2w\cos^2(\phi/2),\qquad |C_2|^2=u^2w^2=B.
\]
Inserting these into (1) gives the stated two-term deficit. Because \(u,v,w>0\), for any gap with \(t_d>0\) the phase minimum is attained exactly at \(\phi=\pi\); for an antipodal gap the phase-dependent term vanishes. This proves the phase portion of the complete equality classification.

**3. Exact finite-grid frequency optimization.** With \(A=v^2(u-w)^2\ge0\), the remaining objective is the strictly convex quadratic
\[
F(t)=At+B(2t-1)^2=4Bt^2+(A-4B)t+B.
\]
On \(t\ge0\) its real minimizer is \(\tau=\max\{0,(4B-A)/(8B)\}\). When \(\tau>0\), completing the square proves that the minimizing sampled \(t_d\) are precisely the closest to \(\tau\). When \(\tau=0\), \(F\) is strictly increasing on nonnegative \(t\), giving the same rule. The values \(t_d\) are strictly decreasing for representative gaps \(1\le d\le\lfloor N/2\rfloor\); hence the rule identifies all ties and excludes all other gaps.

**4. Frame property of all optimizers.** A vanishing eigenvalue would require two distinct unit-circle zeros \(z_1,z_2\) of \(P\), whose ratio is \(\zeta^{\ell_1-\ell_0}\). If both zeros lie on the unit circle, factorization \(P(z)=c(z-z_1)(z-z_2)\) implies
\[
\frac{b^2}{ac}=\frac{(z_1+z_2)^2}{z_1z_2}
=2+2\cos(\arg z_1-\arg z_2)\ge0.
\]
For a non-antipodal optimal gap, \(ac/b^2<0\), a contradiction. For an antipodal gap, the two roots would be negatives of one another and force \(b=0\), also a contradiction. Thus every optimal system has strictly positive eigenvalues and is a frame.

**5. Tightness and explicit phase transition.** Since \(B>0\), equality \(\Phi=4N\) in (1) forces \(2t_d-1=0\); hence \(t_d=1/2\), \(d=N/4\) in the chosen half-range, and \(4\mid N\). Its nonzero \(t_d\) then forces \(C_1=0\), equivalent to \(u=w\) and \(ac/b^2<0\). Conversely these conditions annihilate both terms in (1), proving the exact tightness classification. For \(u=w\), substitute the expression for \(|C_1|^2\) into (1) to obtain the displayed quantitative deficit.

For \(g=(1,1,1)/\sqrt3\), \(A=4/9\), \(B=1/9\); (1) becomes \(\Phi=4N+(8N/9)(1+4t_d^2)\), minimized by the farthest-separated frequencies, with \(\Phi_{\min}=44N/9\) when \(N\) is even. For the sign-flipped window, the lag-one coefficient is zero, so a quarter-cycle gap gives \(4N\) when available. Finally, for \(g=(1,\beta,1)/\sqrt{2+\beta^2}\) with \(\beta>0\), the objective difference from an antipodal gap is a positive multiple of \(t(t+\beta^2-1)\). For even \(N\), the next-smallest grid value is \(\sin^2(\pi/N)\); hence the antipodal gap minimizes precisely when \(\beta^2\ge1-\sin^2(\pi/N)=\cos^2(\pi/N)\), and equality yields the stated tie.

## Verification

The accompanying standalone `CHECK.py` uses only the Python standard library. It constructs all \(2N\) atoms, forms the \(N\times N\) frame operator directly, and compares its Hilbert–Schmidt norm and trace against both the Fourier-eigenvalue formula and the lag-one/lag-two potential identity. It independently checks the complete sampled gap-minimizer rule on many positive magnitude triples and verifies exact tight-frame matrices numerically for explicit quarter-cycle designs. A successful run prints `CHECK_OK assertions=43821` on the supplied deterministic test set. All results are floating-point supplementary checks; the proof above establishes the universal quantifiers analytically.

## Relationship to prior work

Asipchuk, De Carli, and Rodriguez (arXiv:2605.16139, first public May 15, 2026), Corollary 1.2 and its proof, give the general full-translation Gabor diagonalization and frame criterion used in Step 1; these are **not** claimed as new. Their theorem does not give the stated sharp optimization over both phases and pairs of modulation channels at prescribed three-tap magnitudes or the complete associated equality and tightness classification. Magsino (arXiv:1611.00818), Theorem 2.8, gives a general ambiguity-function criterion for tight finite Gabor frames, not the exact constrained energy landscape. Benedetto and Fickus (2003) establish the frame-potential/tightness principle, which is explicitly credited. Related Fourier sampling and finite Riesz design results optimize different Gram matrices (restricted Fourier rows with no full translation orbit), rather than the \(N\)-dimensional two-modulation Gabor frame operator considered here.

## Limitations

The optimization is for frame potential, an average squared spectral deviation, **not** the worst-case frame condition number. It requires exactly two modulation channels, all \(N\) translations, three consecutive nonzero taps, and \(N\ge5\). The analysis does not classify nonoptimal systems, arbitrary tap supports, or higher channel counts. An earlier unindexed equivalent finite-design calculation may exist.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (May 15, 2026), revised arXiv:2605.16139v2 (October 24, 2026). https://arxiv.org/abs/2605.16139
2. M. Magsino, *Constructing Tight Gabor Frames Using CAZAC Sequences*, arXiv:1611.00818v2 (2016). https://arxiv.org/abs/1611.00818
3. J. J. Benedetto and M. Fickus, *Finite Normalized Tight Frames*, Advances in Computational Mathematics 18 (2003), 357–385. DOI: 10.1023/A:1021323312367.
