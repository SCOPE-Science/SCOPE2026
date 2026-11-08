# Periodic predecessor lifting and exact cyclic image counts for elementary cellular automaton Rule 126

## Finding
For each integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous Rule 126 update with cyclic indices. Its output at \(i\) is one exactly when \((x_{i-1},x_i,x_{i+1})\) is not constant. All ring coordinates are indexed: rotations are counted separately, and a predecessor on an \(n\)-ring need not have least period \(n\).

**Theorem (same-period reachability).** A nonconstant cyclic target \(y\) is in \(\operatorname{Im}F_n\) if and only if every maximal cyclic run of ones has length at least two and either some one-run has length at least four or the number of one-runs of length two is even. The all-zero target is always reachable. The all-one target is reachable if and only if \(n\ge2\). Thus avoidance of the familiar `010` Garden-of-Eden factor characterizes *some-period* attainability, but does not always ensure a predecessor on the same ring.

**Theorem (period multipliers, including the boundary exception).** If a target contains cyclic `010`, none of its repetitions has a predecessor. Every other target has a predecessor on the ring of length \(n\) or \(2n\). For a nonconstant `010`-avoider which fails the same-period parity test, the repeated target \(y^k\) has a predecessor on a ring of length \(kn\) **if and only if \(k\) is even**. The exceptional target \(y=1\) on \(n=1\) has no one-symbol predecessor, but \(1^k\) has a predecessor for **every \(k\ge2\)**, including odd \(k\). For all other `010`-avoiding targets a same-period predecessor exists and every repetition is reachable. Hence doubling is a universal sharp upper bound for the first attainable multiplier, but the assertion that *all* failed same-period cases exclude every odd multiplier is false without the exceptional singleton qualification. The words \((011)^{2j+1}\), \(j\ge0\), give an infinite family where precisely even multipliers work.

**Theorem (exact indexed image census).** Write \(R_n=|\operatorname{Im}F_n|\). Let \(\tau_0=3\), \(\tau_1=\tau_2=2\), \(\tau_n=2\tau_{n-1}-\tau_{n-2}+\tau_{n-3}\) for \(n\ge3\); let Lucas numbers satisfy \(L_0=2\), \(L_1=1\), \(L_n=L_{n-1}+L_{n-2}\); put \(\epsilon_n=2\cos(\pi n/2)\) and \(c_n=3(-1)^{n/3}\) when \(3\mid n\), and zero otherwise. Then for every \(n\ge1\),
\[
R_n=\tau_n-\frac{L_n+\epsilon_n-1-c_n}{2}-\mathbf1_{n=1}.
\]
For \(p(z)=1-2z+z^2-z^3\) and \(b(z)=z^3(1+z)/(1-z)\),
\[
\sum_{n\ge1}R_nz^n=-\frac{zp'(z)}{p(z)}-\frac{zb'(z)}{2(1-b(z))}-\frac{3z^3}{2(1+z^3)}-z.
\]
The first nineteen counts are
`1, 2, 2, 6, 12, 23, 37, 66, 119, 217, 387, 693, 1237, 2207, 3927, 6986, 12412, 22028, 39047`.
If \(\lambda\approx1.75487766624669\) is the positive real root of \(t^3-2t^2+t-1\), then
\[
R_n=\lambda^n-\frac12\varphi^n+O(1),\qquad \varphi=(1+\sqrt5)/2.
\]

## Assumptions and definitions
Rule 126 maps neighborhoods `001`, `010`, `011`, `100`, `101`, `110` to one and `000`, `111` to zero. The definition applies literally to degenerate rings \(n=1,2\), where neighboring positions may coincide. A repeated target \(y^k\) has length \(kn\); no claim that its input has primitive period \(kn\) is made. The result concerns one synchronous time step, not eventual images, attractors, noise or individual predecessor multiplicities.

## Proof

**1. Cyclic XOR boundaries.** Define \(d_i=x_i\oplus x_{i+1}\). Checking the eight local triples gives
\[
(F_n(x))_i=d_{i-1}\lor d_i.
\]
Every binary input has \(\sum_i d_i\equiv0\pmod2\), because the cyclic XOR telescopes. Conversely, every even-weight cyclic boundary word integrates to precisely two inputs: choose \(x_0\in\{0,1\}\) and recursively set \(x_{i+1}=x_i\oplus d_i\); even parity closes the cycle. Hence target reachability is precisely the existence of a compatible **even-weight** boundary word \(d\).

**2. Run criterion and constant cases.** A zero output forces both neighboring boundary bits to zero. Thus `010` cannot occur. Between two forced zero boundary bits, an output one-run of length \(\ell\ge2\) has \(\ell-1\) internal boundary bits starting and ending at one, with no adjacent internal zeros. A length-two one-run contributes exactly one one (odd parity); a length-three run contributes exactly two ones (even parity). At length at least four there are allowed fillings of either parity: the all-ones interior and the same interior with exactly one nonendpoint zero. Different runs have independent boundary choices. This gives the criterion for nonconstant targets. For \(y=0^n\), choose \(d=0^n\). For \(y=1^n\), the boundary word must have no adjacent zeros: if \(n\) is even take all ones, and if \(n\ge3\) is odd take exactly one zero; these words have even weight. For \(n=1\), the sole even boundary bit is zero, so the one-symbol output is unreachable.

**3. Exact lifting periods.** If `010` appears, the local OR condition fails on every repetition. A nonconstant `010`-avoider that fails same-period reachability has every one-run of length two or three, with an odd number of two-runs. Each one-run filling is then uniquely forced; its odd parity repeats \(k\) times, and an even boundary word exists exactly for even \(k\). Thus doubling gives a predecessor and no odd multiplier works. For the *exceptional* one-symbol target `1`, on the repeated length-\(k\) ring use the constant-one boundary word when \(k\) is even, or a word with exactly one zero when odd \(k\ge3\). Both have even Hamming weight and no adjacent zeros; \(k=1\) cannot work. This constructs odd-multiplier predecessors such as input `001` producing target `111`. If the original target is reachable, repeating its even boundary word yields a predecessor for each \(k\ge1\). The family \((011)^{2j+1}\) has an odd number of forced two-runs and demonstrates sharp period doubling at infinitely many lengths.

**4. Count `010`-avoiding cyclic outputs.** The directed overlap graph on pair states `00`, `01`, `10`, `11`, excluding the triple `010`, has adjacency matrix
```
[[1,1,0,0], [0,0,0,1], [1,1,0,0], [0,0,1,1]].
```
Each cyclic indexed word corresponds bijectively to a length-\(n\) closed walk, even for small \(n\). Its trace \(\tau_n\) is determined by \(\det(I-zT)=1-2z+z^2-z^3=p(z)\), whence \(\sum_{n\ge1}\tau_nz^n=-zp'(z)/p(z)\).

**5. Count parity-obstructed words.** A nonconstant `010`-avoider without any one-run of length at least four is a cyclic concatenation of nonempty zero-runs and one-runs of lengths two or three. The block generating function is
\[
b(z)=\frac{z}{1-z}(z^2+z^3)=\frac{z^3(1+z)}{1-z}.
\]
Marking a block start in an indexed cyclic word gives a factor \(m/n\) for \(m\) blocks on \(n\) indexed sites, so the total cyclic block count has generating function \(zb'(z)/(1-b(z))\). This remains valid for rotationally periodic words because there are exactly \(m\) marked block starts among the \(n\) positions. Since \(1-b(z)=(1+z^2)(1-z-z^2)/(1-z)\), this count equals \(L_n+\epsilon_n-1\). Give each two-run block a sign \(-1\) and each three-run block sign \(+1\). The signed block series becomes \(\widetilde b(z)=z(-z^2+z^3)/(1-z)=-z^3\); its cyclic count has series \(z\widetilde b'(z)/(1-\widetilde b(z))=-3z^3/(1+z^3)\) and coefficient \(c_n\). Therefore exactly \((L_n+\epsilon_n-1-c_n)/2\) cyclic indexed targets have forced odd parity. Subtract these from \(\tau_n\) and additionally subtract the singleton `1` at \(n=1\), yielding the formula for \(R_n\). The rational generating function follows. The nonzero overlap eigenvalues are the roots of \(t^3-2t^2+t-1\); the conjugate roots have modulus \(\lambda^{-1/2}<1\). The Lucas Binet formula and bounded periodic corrections give the asymptotic.

## Verification, originality and limitations
The adjacent `verify.py` independently computes direct Rule-126 images through length 18, confirms their exact counts and run criterion, checks the overlap trace through length 120, and constructs same-period or doubled-period predecessors for all locally allowed targets through length 13. These finite checks support the all-length proof but do not replace it. The revised multiplier statement is also checked directly at the previously missed boundary: the `1` target on the one-ring has no predecessor, while `111` on the three-ring is the image of `001`.

Martínez, Adamatzky, Seck-Tuoh-Mora and Alonso-Sanz (2010; publicly posted as arXiv:1212.0124v1 on 2012-12-01) discuss finite Rule-126 basins, de Bruijn diagrams, and McIntosh's known forbidden `010` factor. OEIS A269173 contains the classical local bitwise formula. Neither the local identity nor `010` avoidance alone is claimed as new. The proposed contribution is the exact same-period parity classification **with the singleton qualification**, the sharp doubling phenomenon for nonconstant obstructed words, and the all-length indexed image census. The complete 2009 McIntosh monograph was not available for direct examination, so historical priority remains qualified.

References: Martínez et al., *How to make dull cellular automata complex by adding memory: Rule 126 case study*, arXiv:1212.0124v1, https://arxiv.org/html/1212.0124v1; McIntosh, *One Dimensional Cellular Automata* (2009, full text not inspected); OEIS A269173, https://oeis.org/A269173; Wolfram, *Statistical Mechanics of Cellular Automata*, Rev. Mod. Phys. 55 (1983), 601–644.
