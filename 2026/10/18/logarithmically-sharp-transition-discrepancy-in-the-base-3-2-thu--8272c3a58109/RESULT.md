# Logarithmically sharp transition discrepancy in the base-\(3/2\) Thue–Morse word

## Finding

Let \(t_0=0\) and define the infinite binary sequence \(t=(t_n)_{n\ge0}\) by
\[
t_{3m}=t_{3m+1}=t_{2m},\qquad t_{3m+2}=1-t_{2m+1}\quad(m\ge0).
\]
For \(N\ge1\), write
\[
C(N)=\sum_{i=0}^{N-2}(t_i\oplus t_{i+1}),\qquad E(N)=5C(N)-2(N-1),
\]
where an empty sum is zero and \(\oplus\) is binary exclusive-or. For each integer \(j\ge1\), put \(\varepsilon_j=j\bmod2\) and define
\[
a_j=\frac{4^{j+\varepsilon_j}-1}{5},\qquad
b_j=\frac{4^{\varepsilon_j}9^j-1}{5}.
\]
Then both are positive integers with \(a_j<b_j\le9^j\), and their normalized transition-count discrepancies satisfy the exact identity
\[
\boxed{E(b_j)-E(a_j)=2j.}
\]
Moreover, every integer \(N\ge2\) satisfies
\[
\boxed{|E(N)|\le2\bigl(1+\log_{9/4}(N-1)\bigr).}
\]
Consequently the maximal absolute error in the empirical frequency of adjacent changes has **sharp logarithmic order**:
\[
\boxed{\max_{1\le n\le N}\left|C(n)-\frac25(n-1)\right|=\Theta(\log N).}
\]
More explicitly, for every \(N\ge9\),
\[
\frac{\lfloor\log_9 N\rfloor}{5}\le
\max_{1\le n\le N}\left|C(n)-\frac25(n-1)\right|
\le\frac25\bigl(1+\log_{9/4}(N-1)\bigr).
\]
This determines the *order* of the worst finite-prefix transition discrepancy, not the optimal leading logarithmic coefficient.

## Assumptions and scope

All indices are nonnegative integers and every factor occurrence, transition, or prefix is measured in the ordinary one-sided infinite word. The recurrence uniquely determines \(t\) after fixing \(t_0=0\). The word is the normalized base-\(3/2\) Thue–Morse word studied by Cassaigne, Espinoza, Rigo, and Stipulanti [1], not Dekking's differently normalized sibling word [2]. The letter \(1\) in the difference word \(y_i=t_i\oplus t_{i+1}\) means an adjacent change. This work concerns the discrepancy in the count of those changes, not the exact separate frequencies of every factor of length two.

## Proof

**1. Exact prefix-count recursion.** Put \(y_i=t_i\oplus t_{i+1}\). Applying the defining recurrence to three consecutive positions gives, for all \(m\ge0\),
\[
y_{3m}=0,\quad y_{3m+1}=1-y_{2m},\quad y_{3m+2}=1-y_{2m+1}.
\]
These are the first-difference identities observed in [1, Section 2.1]. Summing complete triples, including the appropriate final one or two symbols, yields
\[
\begin{aligned}
C(3m)&=2m-1-C(2m) &&(m\ge1),\\
C(3m+1)&=2m-C(2m+1) &&(m\ge0),\\
C(3m+2)&=2m-C(2m+1) &&(m\ge0).
\end{aligned}
\]
The case \(m=0\) in the middle equality is the identity \(C(1)=0\). Subtracting the frequency benchmark gives, for every \(n\ge2\),
\[
\begin{aligned}
E(3m)&=-E(2m)-1,\\
E(3m+1)&=-E(2m+1),\\
E(3m+2)&=-E(2m+1)-2.
\end{aligned}
\]
The initial value is \(E(1)=0\).

**2. Two-scale contraction and logarithmic upper bound.** Applying those relations twice gives the uniform nine-to-four recursion
\[
E(9m+r)=E(4m+u_r)+v_r,
\]
where the offsets are exactly:

| \(r\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(u_r\) | 0 | 1 | 1 | 1 | 2 | 2 | 3 | 3 | 3 |
| \(v_r\) | 0 | 0 | −2 | 1 | 1 | −1 | −1 | 2 | 0 |

The first-step index map is \(h(3m)=2m\), \(h(3m+1)=h(3m+2)=2m+1\). It satisfies \(h(n)-1\le\frac23(n-1)\) for \(n\ge1\). The table shows \(|E(n)-E(h(h(n)))|\le2\) and the corresponding distance to the base index decreases by at least a factor \(4/9\). Thus for \(n\ge2\), after at most \(1+\lfloor\log_{9/4}(n-1)\rfloor\) two-step reductions we reach \(1\). Every reduction changes \(E\) by at most two. Because \(E(1)=0\), this proves
\[
|E(n)|\le 2\bigl(1+\log_{9/4}(n-1)\bigr).
\]

**3. Exact repunit resonance.** The \(r=7\) entry of the table is
\[
E(9m+7)=E(4m+3)+2\qquad(m\ge0).
\]
Consequently, whenever a positive integer \(u\) is congruent to \(3\) modulo \(4\), its successor \(g(u)=(9u+1)/4\) is an integer and satisfies \(E(g(u))=E(u)+2\). Notice the exact multiplier identity
\[
5g(u)+1=\frac94(5u+1).
\]
For the stated \(a_j\), \(5a_j+1=4^{j+\varepsilon_j}\). Hence, inductively, for every \(0\le i\le j\),
\[
5g^{i}(a_j)+1=9^i4^{j+\varepsilon_j-i}.
\]
For \(i<j\) the right-hand side is divisible by four; since five is congruent to one modulo four, \(g^{i}(a_j)\equiv3\pmod4\). Therefore all \(j\) steps are legal. At the end,
\[
g^j(a_j)=\frac{4^{\varepsilon_j}9^j-1}{5}=b_j,
\]
and repeated use of the \(r=7\) formula yields \(E(b_j)-E(a_j)=2j\). The integer \(a_j\) is positive, \(g(u)>u\) for every positive \(u\), and \(b_j<9^j\), proving the claimed endpoint bounds.

**4. Optimal growth order.** If two real numbers differ by \(2j\), at least one has absolute value at least \(j\). Thus the explicit endpoints show \(\max_{1\le n\le9^j}|E(n)|\ge j\). For arbitrary \(N\ge9\), choose \(j=\lfloor\log_9 N\rfloor\). Monotonicity of the maximal absolute discrepancy and the upper bound from step 2 give the two-sided inequality in the finding, hence the \(\Theta(\log N)\) law.

## Verification

The standalone standard-library script `verification/check_discrepancy.py` generates the first 150,000 letters of \(t\) from its original two-to-three recurrence. It separately computes \(E(N)\) by the derived one-step recursion and compares every finite prefix count, with no sampling. It also exhaustively checks every nine-to-four table entry, distance contraction, and offset bound up to 150,000. Finally it verifies the exact repunit-gap identities for \(1\le j\le120\) using unbounded Python integers and explicitly replays each permitted \(r=7\) transformation. The recorded output is in `verification/check_output.txt`. These finite computations are corroboration: the argument in the proof establishes the infinite assertions.

## Relationship to prior work

Cassaigne–Espinoza–Rigo–Stipulanti [1] prove that the difference word is a \((9,4)\)-Toeplitz word and already compute its limiting density of ones as \(2/5\) (Proposition 11 and its subsequent computation). Their recurrence for individual differences is the starting point of the present argument; neither that density nor the first-difference recurrence is claimed as new. The additional assertion here is an explicit unbounded, exactly quantified discrepancy contrast between two arithmetic families of prefix lengths, together with a matching logarithmic *order* bound. Their full available preprint's discussion of frequencies and Toeplitz structure does not state a finite-prefix oscillation theorem. Dekking [2] treats a differently normalized sibling sequence. General Toeplitz factor-complexity results cited by [1] do not themselves determine this exact repunit contrast.

## Limitations

The theorem proves sharp logarithmic **order**, not the exact maximal discrepancy, the best leading coefficient, or the individual discrepancy at either member of each explicit pair. In particular, the equation \(E(b_j)-E(a_j)=2j\) alone does not specify which endpoint has the larger absolute error. The result uses the base-\(3/2\) binary sequence in [1], not every rational-base generalization. The arithmetic argument is a self-review; it has not undergone independent expert validation. Historical priority beyond the examined accessible primary literature remains to be checked.

## References

[1] J. Cassaigne, B. Espinoza, M. Rigo, and M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base \(3/2\) and related conjectures*, arXiv:2602.21895, first posted 2026-02-25. https://arxiv.org/abs/2602.21895 .

[2] F. M. Dekking, *The Thue–Morse sequence in base \(3/2\)*, Journal of Integer Sequences 26 (2023), Article 23.2.3, arXiv:2301.13563. https://arxiv.org/abs/2301.13563 .
