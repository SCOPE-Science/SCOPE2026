# Exact state complexity of every shift of the binary powers-of-two indicator

## Finding

Let \(P(n)\) equal \(1\) when the nonnegative integer \(n\) is a positive power of two and \(0\) otherwise. For each integer \(c\ge 1\), define \(N(c)\) as the number of states in the **minimal complete binary DFA with output** that, on every finite binary word \(w\), read most-significant digit first, returns \(P([w]_2+c)\). Leading zeros and the empty word are permitted; \([\varepsilon]_2=0\).

Put \(s=\lfloor\log_2 c\rfloor+1\). If \(c\) is a power of two, then

\[
N(c)=s+2.
\]

Otherwise write \(b=2^s-c\), let \(\alpha\) be the canonical binary representation of \(b\), let \(\ell=|\alpha|\), and let \(\beta=0^{s-\ell}\alpha\), its length-\(s\) left-zero-padded representation. Write \(\alpha=1^r u\), where \(r\ge1\) is the complete initial run of ones and either \(u=\varepsilon\) or \(u\) starts with zero. Finally, let \(h=\operatorname{lcp}(u,\beta)\), the *length* of their longest common prefix. Then

\[
\boxed{N(c)=s+r+h+3.}
\]

In particular, for every integer \(s\ge2\) and \(2^{s-1}<c<2^s\),

\[
s+4\le N(c)\le 2s+2,
\]

with both ends sharp: \(c=2^s-1\) attains the lower bound and \(c=2^{s-1}+1\) attains the upper bound.

## Assumptions and scope

A complete DFAO is a deterministic finite automaton with all letter transitions defined, with outputs in \(\{0,1\}\). Its output is that of the terminal state. State count includes any reachable rejecting sink. Minimal means minimal among all such complete DFAOs representing the prescribed function on *every* binary word, including arbitrarily many leading zeros. The binary representation of zero is permitted to be empty; \(P(0)=0\), while \(P(c)\) may be \(1\). State equivalence is equality of all continuation-output functions, equivalently the Myhill–Nerode equality of right quotients of the language on which output is \(1\). The two branches above cover every \(c\ge1\); the dyadic envelope applies to non-powers only.

## Proof

**Step 1: The exact accepted language.** Suppose first that \(c\) is not a power of two. Its binary length is \(s\) and \(2^{s-1}<c<2^s\), so \(b=2^s-c\) satisfies \(1\le b<2^{s-1}\). Thus \(\ell\le s-1\) and \(\beta\) starts with zero. For any \(k\ge s\), the nonnegative number \(2^k-c\) has binary representation \(\alpha\) if \(k=s\), and \(1^{k-s}\beta\) if \(k>s\). These are all powers of two strictly above \(c\), hence all accepted numbers. Allowing leading zeros gives the language

\[
\mathcal L_c=0^*\bigl(\{\alpha\}\cup1^+\beta\bigr).
\tag{1}
\]

When \(c=2^{s-1}\) is a power, the accepted numbers additionally include zero (obtained at the exponent \(s-1\)); for larger exponents their binary forms are \(1^j0^{s-1}\), \(j\ge1\). Therefore

\[
\mathcal L_c=0^*\bigl(\{\varepsilon\}\cup1^+0^{s-1}\bigr).
\tag{2}
\]

**Step 2: Counting right quotients in (1).** For a binary word \(v\), its right quotient is \(v^{-1}\mathcal L_c=\{z:vz\in\mathcal L_c\}\). Let \(I=1^*\beta\); it is an infinite language because \(\beta\) begins with zero. Prefixes consisting entirely of zeros have quotient \(\mathcal L_c\). Any prefix with an impossible continuation has quotient \(\varnothing\). Because \(\alpha\) begins with \(r\) consecutive ones, the remaining right quotients fall into the following exhaustive classes:

1. Exactly \(r\) infinite two-branch quotients \(I\cup\{\alpha[j:]\}\), for \(1\le j\le r\), reached after \(1^j\). Here \(\alpha[j:]\) denotes its suffix after its first \(j\) digits. An initial block of more than \(r\) ones loses the exceptional finite word \(\alpha\) and gives the single infinite quotient \(I\).
2. Exactly \(h\) finite *two-word* quotients \(\{\beta[d:],\alpha[r+d:]\}\), for \(1\le d\le h\). They are reached after \(1^r\beta[:d]\), precisely while the respective continuations still agree. The two suffixes differ in length by \(s-\ell+r>0\), so each such quotient really has two elements.
3. Exactly \(s\) finite singleton quotients \(\{\beta[d:]\}\), for \(1\le d\le s\), reached after a sufficiently long block of initial ones and the first \(d\) digits of \(\beta\). When the exceptional branch \(\alpha\) diverges or terminates, any additional exceptional-only suffix is a suffix of \(\alpha\), hence already a suffix of \(\beta=0^{s-\ell}\alpha\), and introduces no new quotient.

To verify exhaustiveness, delete any initial zero padding, then follow either the finite word \(\alpha\) or the infinite family \(1^+\beta\). Before the first zero, the quotient is of type 1 (or \(I\)); after the first zero, at most two distinct suffix candidates survive, and both survive exactly during the common-prefix interval of length \(h\), of type 2. Every remaining nonempty quotient is type 3.

These quotients are pairwise distinct: \(\mathcal L_c\) is the only quotient with arbitrary initial zero padding; \(\varnothing\) is empty; the \(r+1\) infinite quotients \(I\) and \(I\cup\{\alpha[j:]\}\) differ by exceptional words of distinct lengths less than \(s\); the \(h\) two-element quotients are distinct since their longer words \(\beta[d:]\) have distinct lengths; and the \(s\) singleton quotients are distinguished by the distinct lengths \(s-d\) of their only words. An infinite quotient is not a finite quotient, and a two-element one is not a singleton. The complete minimum has exactly

\[
1\;(\mathcal L_c)+1\;(\varnothing)+(r+1)\;(\text{infinite})+h\;(\text{pairs})+s\;(\text{singletons})=s+r+h+3
\]

states. Every listed quotient is reachable by the displayed prefixes, so this is both a lower and an upper bound by the Myhill–Nerode theorem.

**Step 3: The power-of-two case.** In (2), the right quotients are the root \(\mathcal L_c\), the empty set, the infinite quotient \(1^*0^{s-1}\) after one initial one, and the \(s-1\) distinct singleton suffixes of \(0^{s-1}\) after consuming one or more of its zeros. For \(s=1\), the latter class is empty and the infinite quotient is \(1^*\), distinct from \(0^*1^*\). Thus the count is \(2+1+(s-1)=s+2\) for all \(s\ge1\).

**Step 4: Sharp dyadic range.** For nonpowers, \(1\le r\le\ell\le s-1\) and \(0\le h\le\ell-r\). Therefore \(1\le r+h\le s-1\), yielding the bounds. When \(c=2^s-1\), \(\alpha=1\), \(r=1\), \(h=0\), so \(N(c)=s+4\). When \(c=2^{s-1}+1\), \(\alpha=1^{s-1}\), \(r=s-1\), \(h=0\), so \(N(c)=2s+2\). Both are nonpowers for \(s\ge2\). This completes the proof.

## Verification

The standalone `shifted_powers_checker.py` constructs an independent nondeterministic word-acceptor directly from the languages (1) and (2), determinizes it including a dead state, and minimizes by output-refining transition partitions. It compares the resulting exact state count with the formula for every integer shift from \(1\) through \(4095\). Independently, for the first \(100\) shifts and each index from \(0\) through \(179\), it compares the automaton's output with direct integer arithmetic, both on canonical and zero-padded inputs. The saved output `shifted_powers_checks.txt` records the results. These finite checks guard against transcription errors; the proof above establishes the result for every shift.

## Relationship to prior work

Moradi, Rampersad, and Shallit (2025 preprint; revised 2026) proved in their Theorem 21 that this exact shifted powers-of-two sequence admits a most-significant-digit-first automaton with \(O(\log c)\) states. Their construction and qualitative bound establish neither the minimal exact count nor its sharp bit-dependent dyadic range. The present result studies their same sequence and encoding, counts minimal complete states including the dead state, and proves a matching formula by classification of all distinct right quotients. Moradi, Popoli, Shallit, and Vukusic (2026) study shifted Fibonacci words and cite logarithmic growth for the powers-of-two example; their different underlying sequence does not imply this formula. General treatments of operations on automatic sequences, including Zantema and Bosma (2022), do not provide this bitwise classification.

## Limitations

The theorem concerns ordinary binary most-significant-digit-first input with arbitrary leading zeros and *complete* automata. Removing an implicit dead state, disallowing padding, reading least-significant digits first, changing the base, or marking powers including other conventions may change state counts. The result is a self-contained mathematical theorem with supporting finite checks, not an independently audited or machine-formalized proof. Full originality relative to unindexed or differently phrased prior literature cannot be guaranteed.

## References

1. D. Moradi, N. Rampersad, and J. Shallit, “Complexity of Linear Subsequences of \(k\)-Automatic Sequences,” arXiv:2512.10017, originally submitted 2025-12-10, §4.3 and Theorem 21. https://arxiv.org/abs/2512.10017
2. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, “State Complexity of Shifts of the Fibonacci Word,” arXiv:2603.18858, 2026-03-19. https://arxiv.org/abs/2603.18858
3. H. Zantema and W. Bosma, “Complexity of Automatic Sequences,” 2022, sections on tails and transformed sequences.
