# Exact two-summand complement and optimal short witness for even Zeckendorf weight

## Finding

Let \(F_1=1\), \(F_2=2\), and \(F_{j+2}=F_{j+1}+F_j\). Let \(s_F(n)\) be the number of nonzero digits in the unique expansion of \(n\) as a sum of nonconsecutive terms from these Fibonacci weights, with \(s_F(0)=0\). Set \(E=\{n\ge0:s_F(n)\equiv0\pmod2\}\).

**Theorem.** The exact two-summand complement is
\[
\mathbb N_0\setminus(E+E)=\{1,2,3,5\}.
\]
In fact, every integer \(n\ge6\) has \(n=a+b\) with \(a,b\in E\) and
\[
a\in\{0,4,6,7,9,10\}.
\]
The constant \(10\) is optimal: if \(B\) is the smallest nonnegative integer such that every \(n\ge6\) admits \(n=a+b\) with \(a,b\in E\), \(0\le a\le B\), then \(B=10\).

## Assumptions and scope

All indices and summands are nonnegative integers; repeated and zero summands are allowed. The Zeckendorf expansion is the canonical one with no adjacent nonzero Fibonacci weights. Both the exact exception set and the sharp short-summand bound concern **even Zeckendorf digit weight**; they do not assert analogous facts for odd weight or for ordinary binary digit weight.

## Proof

**Parity-word recursion.** Define finite binary words \(W_1=0\), \(W_2=01\), and, for \(j\ge2\),
\[
W_{j+1}=W_j\,\overline{W_{j-1}},
\]
where the bar exchanges zero and one and juxtaposition means concatenation. The word \(W_j\) has length \(F_j\), and its letter at position \(m\), starting from position zero, equals \(s_F(m)\pmod2\) for \(0\le m<F_j\). Indeed, the interval \([0,F_{j+1})\) splits into \([0,F_j)\) and \([F_j,F_{j+1})\); in the latter interval the leading Fibonacci weight contributes one digit and the allowed remainder lies in \([0,F_{j-1})\). Hence the latter block is the bitwise complement of \(W_{j-1}\). The words form nested prefixes and define an infinite word \(w\).

**Certified finite-factor lemma.** Let \(\mathcal F\) be the set of all length-\(21\) factors of \(W_{13}\). Direct finite enumeration using the appended exact verifier establishes the following equalities and containments:

1. \(|W_{13}|=377\), and \(|\mathcal F|=132\). The length-\(21\) factors of \(W_{14}\) are exactly \(\mathcal F\).
2. \(\mathcal F\) is invariant under digit complementation.
3. Every \(W_j\), \(j\ge13\), starts with the same length-\(20\) prefix \(P=01110100100011000101\). Its length-\(20\) suffix follows a four-periodic cycle. The four successive suffixes at indices \(13,14,15,16\) are
   `00010110111001110100`, `11101000111010010001`, `11101001000110001011`, `00010111000101101110`.
4. For each of these four suffixes \(S\), all \(20\) length-\(21\) windows crossing the join in \(S\overline P\) belong to \(\mathcal F\).
5. Every \(t\in\mathcal F\) contains a zero in at least one of the six positions \(20-a\), where \(a\in\{0,4,6,7,9,10\}\).

Here is why this **finite certificate proves an infinite statement**. The recurrence implies that the length-\(20\) suffix \(S_{j+2}\) is \(\overline{S_j}\) whenever \(j\ge13\), hence \(S_{j+4}=S_j\); the displayed four cases are exhaustive. Induct on \(j\ge14\) to show that every length-\(21\) factor of \(W_j\) belongs to \(\mathcal F\). The two base cases are \(W_{13},W_{14}\). Internal factors of \(W_j\) and \(\overline{W_{j-1}}\) are covered by induction and complementation invariance. A factor crossing the join lies among the twenty checked windows of one of the four boundary types. Thus every length-\(21\) factor of the infinite word \(w\) belongs to \(\mathcal F\). These are finite equality checks, not a claim that a finite numerical search proves the theorem without the induction.

**Uniform representation.** The six integers \(0,4,6,7,9,10\) all belong to \(E\), as seen directly from their canonical Fibonacci expansions. For any \(n\ge20\), apply item 5 to \(w[n-20]\cdots w[n]\). There is some listed \(a\) with \(w[n-a]=0\); hence \(a,n-a\in E\), and \(n=a+(n-a)\). For \(6\le n<20\), direct exact enumeration in the verifier supplies a representation with a listed \(a\).

**Exceptions and sharpness.** For \(0\le n<6\), the only numbers in \(E+E\) are \(0\) and \(4\), by direct checking of the canonical representations, so the exceptions are precisely \(1,2,3,5\). For \(n=34\), the only members of \(E\) below \(10\) are \(0,4,6,7,9\), while \(34\), \(30\), \(28\), \(27\), \(25\) all have odd Zeckendorf digit weight. Thus no summand \(a<10\) works. Yet \(34=10+24\) and both \(10\) and \(24\) have even Zeckendorf digit weight. Consequently the uniform bound \(10\) is sharp.

## Verification

Execute `python3 verify.py` in the directory containing this result and the bundled script. The program computes the \(132\) factors exactly from the recurrence, checks complementation closure, the four boundary-factor cases, all \(132\) covering witnesses, the small exceptions, and optimality at \(34\). It also checks \(10{,}000\) values independently using the Zeckendorf greedy algorithm; these extra finite checks are not used in the infinite induction.

## Relationship to prior work

Rajasekaran, Shallit, and Smith (first published May 2019) developed finite-automaton methods for additive problems, including a published figure explicitly concerning sums of two **Fibonacci-odd** integers. The present assertion instead treats even Fibonacci/Zeckendorf digit weight, with an exact complement and an optimal bounded small-summand witness. The freely accessible publisher abstract and figure captions do not establish whether the article elsewhere treats that even-weight counterpart; the full article was not separately accessible for comparison. Shallit's 2022 paper studies the **same parity word** but determines its maximum-order complexity rather than its additive two-summand complement or sharp bounded witness. See references. The earlier papers supply context and techniques but no inspected theorem implying the stated bound \(10\).

## Limitations

This theorem concerns only parity of Zeckendorf digit weight and sums of two members of its even class. It does not enumerate the total number of representations or extend the optimal small-summand bound to higher moduli or other numeration systems. Independent examination of the complete 2019 article remains necessary to exclude possible implicit previous coverage; absence of matching search results is not proof of publication priority.

## References

1. A. Rajasekaran, J. Shallit, T. Smith, *Additive Number Theory via Automata Theory*, Theory of Computing Systems **64** (2020), 542–567, initially public 2019-05-29, DOI: https://doi.org/10.1007/s00224-019-09929-9.
2. J. Shallit, *Note on a Fibonacci Parity Sequence*, arXiv:2203.10504v1, initially public 2022-03-20, https://arxiv.org/abs/2203.10504.
3. OEIS A095076, Fibonacci–Thue–Morse (Zeckendorf parity) sequence, https://oeis.org/A095076.
