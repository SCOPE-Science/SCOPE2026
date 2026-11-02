# Parity-dependent critical degeneracy in the uniform antiferromagnetic Ising wheel under a field

## Finding
For a wheel made from one hub and an \(n\)-site ring, homogeneous nearest-neighbor antiferromagnetic interactions and a homogeneous longitudinal field produce a sharp parity-dependent first magnetization transition. For odd \(n\ge5\), the first transition is exactly at \(|h|=J\) and carries \(L_n+2n\) ground states, where \(L_n\) is the \(n\)-th Lucas number. For even \(n\ge4\), the first transition moves to \(|h|=nJ/(n-2)\) and carries exactly three ground states. Both parities saturate at \(|h|=nJ\). This gives a positive critical residual entropy \(\log\varphi\) per spin along the odd subsequence but zero along the even critical subsequence, where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
Let \(n\ge4\) be an integer, \(J>0\), and \(h\in\mathbb R\). The wheel is \(W_{n+1}=K_1\vee C_n\), with hub spin \(t\in\{-1,+1\}\), rim spins \(s_i\in\{-1,+1\}\) indexed modulo \(n\). Define
\[
H=J\left(\sum_{i=0}^{n-1}s_i s_{i+1}+t\sum_{i=0}^{n-1}s_i\right)-h\left(t+\sum_{i=0}^{n-1}s_i\right).
\]
All bonds, including the spokes, have the same positive antiferromagnetic strength. Put \(x=|h|/J\) and let \(g_n(x)\) count *labeled spin configurations* at the exact ground energy (rotations and spin reversals are not identified). Let \(L_n=\varphi^n+(1-\varphi)^n\) be the Lucas number, so \(L_0=2,L_1=1\).

For **odd \(n\ge5\)**, the exact normalized ground energy is
\[
E_n/J=\begin{cases}-(n-1)&0\le x\le1,\\-(n-1)x&1\le x\le n,\\2n-(n+1)x&x\ge n.\end{cases}
\]
The degeneracies are \(g_n=2n\) for \(0\le x<1\), \(g_n(1)=L_n+2n\), \(g_n=1\) for \(1<x<n\), \(g_n(n)=2\), and \(g_n=1\) for \(x>n\).

For **even \(n\ge4\)**, define \(x_c=n/(n-2)\). Then
\[
E_n/J=\begin{cases}-n-x&0\le x\le x_c,\\-(n-1)x&x_c\le x\le n,\\2n-(n+1)x&x\ge n.\end{cases}
\]
The degeneracies are \(g_n(0)=4\), \(g_n=2\) for \(0<x<x_c\), \(g_n(x_c)=3\), \(g_n=1\) for \(x_c<x<n\), \(g_n(n)=2\), and \(g_n=1\) for \(x>n\). The formulas at shared boundaries agree. Negative fields are covered by global spin reversal. The special rim length \(n=3\) is excluded because the wheel then becomes a complete graph and has extra symmetry.

## Proof
**1. Exact ring lemma.** Fix a field \(B\in\mathbb R\) and consider a cycle of \(n\ge4\) spins with normalized energy \(Q_B=\sum_i s_i s_{i+1}-B\sum_i s_i\). Its minimum and number of minimizers are:

- For \(n\) even: if \(|B|<2\), the minimum is \(-n\), with two alternating minimizers; at \(|B|=2\), the minimum is \(-n\), with \(L_n\) minimizers; for \(|B|>2\), the minimum is \(n-n|B|\), with one uniform minimizer.
- For \(n\) odd: at \(B=0\), the minimum is \(-(n-2)\), with \(2n\) minimizers; for \(0<|B|<2\), the minimum is \(-(n-2)-|B|\), with \(n\) minimizers; at \(|B|=2\), the minimum is \(-n\), with \(L_n\) minimizers; for \(|B|>2\), the minimum is \(n-n|B|\), with one uniform minimizer.

To prove this without a thermodynamic-limit argument, by spin reversal assume \(B\ge0\). Let \(k\) be the number of down spins and \(b\) the number of neighboring down/down pairs on the cycle. The exact identity is \(Q_B=n-Bn+2(B-2)k+4b\). If \(B>2\), both nonconstant terms are nonnegative and equality requires \(k=0\). At \(B=2\), equality requires \(b=0\); thus the down sites form an independent set of the cycle, whose number is \(L_n\) by the ordinary independent-set recurrence \(F_{n-1}+F_{n+1}=L_n\). For \(0\le B<2\), counting alternating unlike-spin bonds yields the minimal number of frustrated same-spin bonds: zero for an even cycle and one for an odd cycle. On an odd cycle with \(0<B<2\), the field selects the \(n\) states with one more up spin; at \(B=0\) both spin orientations are allowed, yielding \(2n\). An elementary domain-wall exchange (replace two separated unnecessary equal-spin bonds by alternating bonds, preserving or increasing the field-aligned majority) shows no state with additional frustrated bonds can minimize when \(B<2\); equivalently this follows directly from \(b\ge\max\{0,2k-n\}\) with equality achievable at each \(k\), and minimizing the preceding affine expression over integral \(0\le k\le n\). This proves all cases and the counts.

**2. Conditioning on the hub.** By global spin reversal take \(h\ge0\), set \(x=h/J\), and let \(m_n(B)=\min Q_B\). For hub spin \(t=\pm1\), the rim sees effective field \(B=x-t\), so the exact sector minimum divided by \(J\) is
\[
E_t/J=m_n(x-t)-xt.
\]
The multiplicity in each hub sector equals the multiplicity in the ring lemma. In particular \(E_-/J=m_n(x+1)+x\) and \(E_+/J=m_n(x-1)-x\).

**3. Odd parity.** For odd \(n\ge5\) and \(0\le x<1\), both sectors have minimum \(-(n-1)\), each with \(n\) minimizers (also at \(x=0\)). At \(x=1\), the negative-hub sector is at the ring's \(B=2\) independent-set threshold and has \(L_n\) minimizers, while the positive-hub sector has \(B=0\) and \(2n\) minimizers. For \(1<x<3\), the negative-hub sector has \(E_-/J=-(n-1)x\), whereas the positive-hub sector has \(E_+/J=-n+3-2x\). Their difference is \((n-3)(x-1)>0\), since \(n\ge5\). For \(x\ge3\) the positive-hub sector has energy \(2n-(n+1)x\), exceeding the negative-hub sector by \(2(n-x)\) up to \(x=n\). For \(x>n\), the fully aligned positive-hub state wins. At \(x=n\) exactly two uniform-rim configurations, with opposite hub spins, tie. Thus all odd formulas follow.

**4. Even parity.** At \(x=0\), both hub sectors have two alternating rim minimizers, giving four. For \(0<x<1\), the positive-hub sector has energy \(-n-x\), below the negative-hub value \(-n+x\). At \(x=1\) the positive-hub Néel sector continues to win; for \(1<x<3\) it has \(-n-x\), whereas the negative-hub sector is \(-(n-1)x\). The unique crossing solves \(-n-x=-(n-1)x\), or \(x_c=n/(n-2)\), which belongs to \((1,3)\) for every even \(n\ge4\). There are precisely two alternating rim states with positive hub, and one all-up rim state with negative hub, so the crossing multiplicity is three. For \(x\ge3\), the fully aligned positive-hub sector has energy \(2n-(n+1)x\) and its difference from the negative-hub sector is \(2(n-x)\); this gives saturation at \(x=n\) with exactly two configurations. Together these comparisons complete the proof.

**5. Entropy contrast.** The Lucas relation \(L_n=\varphi^n+(1-\varphi)^n\) implies \(\lim_{n\to\infty,\ n\ \mathrm{odd}}\frac{\log(L_n+2n)}{n+1}=\log\varphi>0\). For even \(n\), the corresponding critical degeneracy is always three, so its entropy per spin tends to zero. The distinction concerns the sequence of finite-system crossing points, not a claim about two different bulk phase transitions.

## Verification
The self-contained Python program `wheel_verify.py` computes exact spectra of spin configurations using rational fields, exhaustively covering all \(2^{n+1}\) configurations for rim lengths \(4\le n\le16\). It independently applies an exact min-plus transfer calculation to all larger selected lengths up to \(202\). It checks energies *and* multiplicities at the crossing fields, saturation, regular fields, and perturbations immediately to either side. The recorded run passed 421 exhaustive comparisons and 448 exact transfer comparisons. These computations corroborate, but do not replace, the preceding all-size proof. Run `python3 wheel_verify.py` in the same directory; it requires only the Python standard library.

## Relationship to prior work
Frustrated triangular Ising systems and domain-wall entropy were studied by Mostovoy, Prokof'ev, Khomskii and Knoester (arXiv:cond-mat/0210711, first public version 31 October 2002). The exact magnetic-field diagram for an infinite zigzag Ising ladder with multisite interactions was studied by Jurčišinová and Jurčišin (2014); that graph and interaction differ from the wheel. Florek and Jaworski's 2023 article concerns ground-state degeneration for antiferromagnetic **Ising wheels** with variable spin magnitudes and coupling ratios, and explicitly uses Fibonacci-like counting. It is the closest identified priority risk. Its accessible publisher preview was inspected, but the full text was not available. The result stated here does **not** claim the independent-set/Lucas count in isolation as new: the candidate contribution is the **complete uniform spin-half, uniform-field, all-rim-length energy and degeneracy classification**, particularly the parity-separated thresholds \(J\) versus \(nJ/(n-2)\). Whether specialized past wheel work contains an equivalent full field classification remains unverified.

## Limitations
The result is restricted to classical spins \(\pm1\), one homogeneous hub, equal spoke/rim antiferromagnetic couplings, exact zero temperature, and a longitudinal field; no finite-temperature or quantum claim is made. The critical entropy is a finite-system crossing-sequence property; no bulk thermodynamic phase-transition distinction is asserted. Priority remains subject to examination of inaccessible specialized wheel ground-state literature. Independent scientific audit has not been performed.

## References
1. M. Mostovoy, N. Prokof'ev, D. Khomskii and J. Knoester, *Frustrated spin model as a hard-sphere liquid*, arXiv:cond-mat/0210711 (first public 2002-10-31). https://arxiv.org/abs/cond-mat/0210711
2. E. Jurčišinová and M. Jurčišin, *Solution of the antiferromagnetic Ising model with multisite interaction on a zigzag ladder*, Phys. Rev. E **90**, 032108 (2014). https://doi.org/10.1103/PhysRevE.90.032108
3. W. Florek and J. Jaworski, *Ground state degeneration of frustrated antiferromagnetic Ising wheels*, Modern Physics Letters B **37**, 2350189 (2023). https://doi.org/10.1142/S0217984923501890
