# Sharp fourth-moment extension and phase stability for binary quadratic conics

## Finding

Let \(q\) be any odd prime power. For every nondegenerate homogeneous binary quadratic form \(Q\) on \(\mathbb F_q^2\) and every \(j\in\mathbb F_q^\times\), the nonzero conic \(S=\{v:Q(v)=j\}\) has cardinality \(M=q-1\) when \(Q\) splits and \(M=q+1\) otherwise. For a nontrivial additive character \(\psi\), put
\[
Tf(\xi)=\sum_{v\in S} f(v)\psi(\xi\cdot v),\qquad \xi\in\mathbb F_q^2.
\]
Equipping input with counting \(\ell^2(S)\) and output with uniform-probability \(L^4(\mathbb F_q^2)\), the **sharp endpoint norm** is
\[
\boxed{\|T\|_{\ell^2\to L^4}^{4}=3-\frac3M.}
\]
Every nonzero extremizer is exactly a function with \(|f(v)|\) constant and positive on \(S\) and with \(f(v)f(-v)\) independent of the antipodal pair. Conversely, all such functions attain equality. Up to nonzero complex scalar, their phase family is a torus of real dimension \(M/2\).

The result includes an **exact, globally nonnegative deficit**. Label the \(k=M/2\) antipodal pairs by \(\{v_i,-v_i\}\), and write
\[
\begin{split}
U&=\sum_{v\in S}|f(v)|^2,\\
s_i&=|f(v_i)|^2+|f(-v_i)|^2,\\
d_i&=|f(v_i)|^2-|f(-v_i)|^2,\\
z_i&=2f(v_i)f(-v_i).
\end{split}
\]
Then
\[
\boxed{\begin{aligned}
\left(3-\frac3M\right)U^2-\|Tf\|_{L^4}^4
={}&\frac32\sum_{i=1}^{k}\left(s_i-\frac Uk\right)^2\\
&+\sum_{i:s_i>0}\left(\frac U{s_i}-\frac12\right)d_i^2\\
&+\sum_{i<j:s_i s_j>0}s_i s_j
\left|\frac{z_i}{s_i}-\frac{z_j}{s_j}\right|^2.
\end{aligned}}
\]
Any term involving a zero pair mass is omitted. Each term on the right is nonnegative; vanishing precisely characterizes the extremizers.

For normalized surface measure \(\sigma=M^{-1}\sum_{v\in S}\delta_v\), defining \(E=M^{-1}T\), with input \(L^2(S,\sigma)\) and output **unnormalized** counting \(\ell^4(\mathbb F_q^2)\), the sharp fourth power is
\[
\boxed{\|E\|_{L^2(\sigma)\to\ell^4}^{4}=
\frac{q^2}{M^2}\left(3-\frac3M\right).}
\]

## Assumptions and scope

The field \(\mathbb F_q\) has odd characteristic, and \(Q\) is nondegenerate with no linear or constant terms. The level \(j\) must be nonzero. Both split and anisotropic (nonsplit) Witt classes are included, over prime fields and arbitrary extension fields. The additive character can be any nontrivial one; the Fourier side is the full dual group, not a restricted frequency subset. For the deficit, \(f\) is any complex-valued function, including one with zeros; \(U=0\) is allowed and produces the zero identity. No claim is made about degenerate forms, zero level, characteristic two, or other extension exponents.

## Proof

**Step 1: finite conic and pair-sum fibers.** Over an odd finite field, a nondegenerate binary homogeneous form is equivalent, up to an invertible linear substitution and a nonzero scalar, either to \(xy\) or to an anisotropic norm form \(x^2-\delta y^2\), with \(\delta\) a nonsquare. In the split case each nonzero first coordinate uniquely determines the second, yielding \(M=q-1\). In the anisotropic case identify \((x,y)\) with \(x+y\sqrt\delta\in\mathbb F_{q^2}\); the norm map \(\mathbb F_{q^2}^\times\to\mathbb F_q^\times\) is surjective with fibers of size \(q+1\).

Set the polar form \(B(a,b)=Q(a+b)-Q(a)-Q(b)\), nondegenerate because \(Q\) is nondegenerate and the characteristic is odd. If \(s\ne0\), the simultaneous conditions \(Q(v)=Q(s-v)=j\) imply \(B(s,v)=Q(s)\). This is a genuine affine line. Its intersection with \(Q(v)=j\) has at most two points: restriction of a quadratic polynomial to a line can be identically \(j\) only if the line direction \(h\ne0\) satisfies \(Q(h)=0\) and \(B(v,h)=0\), whence \(v\in h^\perp=\operatorname{span}(h)\) and \(Q(v)=0\ne j\), a contradiction. The line is invariant under \(v\mapsto s-v\), so each nonzero sum has either exactly one ordered representation \((v,v)\) or exactly two ordered representations \((v,w),(w,v)\), without collisions between different unordered pairs. At zero, the representations are precisely \((v,-v)\), one for each of the \(M\) choices of \(v\).

**Step 2: exact moment.** Orthogonality of all additive characters on \(\mathbb F_q^2\) gives
\[
\|Tf\|_{L^4}^4=\sum_{s\in\mathbb F_q^2}
\left|\sum_{\substack{v,w\in S\\v+w=s}}f(v)f(w)\right|^2.
\]
Put \(a_v=|f(v)|^2\). The nonzero fibers contribute one \(a_v^2\) for every diagonal pair and \(4a_v a_w\) for every unordered distinct **nonantipodal** pair. The zero fiber contributes \(\big|2\sum_i f(v_i)f(-v_i)\big|^2\). Consequently
\[
\begin{aligned}
\|Tf\|_{L^4}^4
&=\sum_v a_v^2+4\sum_{\{v,w\}:\,v\ne w,\,w\ne-v}a_v a_w
 +\left|\sum_i z_i\right|^2\\
&=2U^2-\frac32\sum_i s_i^2+\frac12\sum_i d_i^2
 +\left|\sum_i z_i\right|^2.
\end{aligned}
\]

**Step 3: completing the nonnegative deficit.** Since \(\sum_i s_i=U\) and \(|z_i|^2=s_i^2-d_i^2\), apply the exact weighted-variance identity
\[
U\sum_{i:s_i>0}\frac{|z_i|^2}{s_i}
-\left|\sum_i z_i\right|^2
=\sum_{i<j:s_i s_j>0}s_i s_j
\left|\frac{z_i}{s_i}-\frac{z_j}{s_j}\right|^2.
\]
Combining it with
\[
\frac32\sum_i(s_i-U/k)^2
=\frac32\sum_i s_i^2-\frac{3U^2}{M}
\]
produces the boxed deficit exactly. Every coefficient \(U/s_i-1/2\) is at least \(1/2\) on the positive-mass pairs. For nonzero \(f\), equality forces \(s_i=U/k>0\) for every \(i\), then \(d_i=0\); consequently all \(|f(v)|\) are the same positive number. The variance term vanishes precisely when all \(z_i/s_i\), equivalently all \(f(v_i)f(-v_i)\), agree. Constant inputs attain equality, so the upper bound is sharp. Each antipodal pair contributes two phases, with one common product constraint across \(k\) pairs; therefore the phase family has \(2k-(k-1)=k+1\) real dimensions before and \(k\) after global-phase quotient.

**Step 4: normalization conversion.** For \(E=M^{-1}T\), the output counting fourth moment gains a factor \(q^2/M^4\), while the squared normalized input norm is \(U/M\). Dividing gives the stated factor \(q^2/M^2\).

## Verification

The accompanying standard-library script `artifacts/verify.py` reconstructs split and nonsplit conics over five prime fields and two quadratic extension fields. It enumerates pair-sum fibers and independently evaluates fourth moments by convolution, tests the exact nonnegative deficit identity on arbitrary complex inputs (including sparse and constant cases), and compares selected values directly with additive-character Fourier sums. Its completed invocation reports

`VERIFY_OK fields=7 pair_fiber_classes=7 energy_and_deficit_tests=70 direct_fourier_tests=12 conic_deficit_tests=84`.

The line-intersection lemma, the character-orthogonality identity, and the weighted-variance equality prove the theorem uniformly for all odd prime powers. The finite runs are reproducibility checks, not an infinite search or a proof by enumeration.

## Relationship to prior work

Mockenhaupt–Tao formulated the finite-field Fourier extension problem. Iosevich–Koh obtain the sharp range of dimension-two extension **exponents**, exploiting pair-sum geometry of nondegenerate quadratic surfaces. Koh–Shen extend such estimates to broader plane curves through algebraic intersection arguments. These theorem-level results are not exact finite-field endpoint operator constants with all equality cases, nor do they state the global nonnegative three-component fourth-moment deficit above.

The more recent sharp extension theory of González-Riquelme–Oliveira e Silva principally treats parabolas, paraboloids and higher-dimensional cones. The recent small-field phase-rigidity result for anisotropic **three-dimensional** quadratic spheres concerns a different geometric object: a full two-dimensional surface in \(\mathbb F_q^3\), not a binary quadratic level curve in \(\mathbb F_q^2\). An exact equality/deficit result for conics is not obtained simply by renaming those hypersurface statements. Generic Sidon or additive-energy inequalities alone likewise do not determine the entire equality set and the weighted stability identity without a specific pair-sum-fiber analysis.

## Limitations

Novelty is assessed against identified theorem statements, related public mathematical records, and available primary literature, not certified exhaustively. An older weak-Sidon, conic additive-energy, or finite Fourier inequality may encode a logically equivalent sharp constant or even the entire stability identity under different normalization. The result does not imply corresponding endpoint formulas for arbitrary plane curves, higher-dimensional quadratic hypersurfaces, characteristic two, or zero-radius conics. The positivity identity is global but does not assert a uniform metric distance-to-extremizers estimate after all symmetry quotients. Independent validation has not been performed.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first public 2002-04-18, https://arxiv.org/abs/math/0204234 .
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28, https://arxiv.org/abs/0804.4505 .
3. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1, first public 2010-03-22, https://arxiv.org/abs/1003.4240 .
4. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public 2024-05-26, https://arxiv.org/abs/2405.16647 .
5. *Small-field phase dichotomy for anisotropic sphere extremizers*, public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-small-field-phase-dichotomy-for-anisotropic-sphere-extremizers--973050ba74a9/RESULT.md .
