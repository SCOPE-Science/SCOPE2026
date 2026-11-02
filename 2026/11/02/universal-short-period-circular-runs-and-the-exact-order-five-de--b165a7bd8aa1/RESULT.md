# Universal short-period circular runs and the exact order-five de Bruijn run spectrum

## Finding

Let \(W\) be a \(q\)-ary de Bruijn cycle of order \(n\), with \(q\ge2\), so \(W\) has length \(q^n\) and contains each length-\(n\) word exactly once as a circular factor. A *circular run* is a maximal finite periodic interval in the periodic extension of \(W\), counted by its starting position modulo \(q^n\), whose length is at least twice its least period. Let \(R_{n,p}(W)\) denote the number of these runs having least period \(p\).

Define the primitive-root count
\[
P_q(p)=\sum_{d\mid p}\mu(d)q^{p/d},
\]
where \(\mu\) is the classical Möbius function. For every \(p\ge1\) and \(n\ge2p+1\), the run count is independent of the chosen de Bruijn cycle:
\[
\boxed{R_{n,p}(W)=(q-1)P_q(p)q^{n-2p-1}.}
\]
More precisely, for every integer length \(L\) with \(2p\le L\le n-2\), exactly
\[
\boxed{(q-1)^2P_q(p)q^{n-L-2}}
\]
period-\(p\) runs have length exactly \(L\); the number of such runs with length at least \(n-1\) is exactly \((q-1)P_q(p)\). All circular runs, of any period, have least period strictly smaller than \(n\).

The first nonrigid short-period boundary is visible in the full binary order-five family. Among its exactly \(2{,}048\) cycles up to rotation, every cycle has eight period-one runs and two period-two runs. The entire profile \((R_{5,1},R_{5,2},R_{5,3},R_{5,4})\) has the following complete distribution:

| Period profile | Number of cycles |
|---|---:|
| \((8,2,2,0)\) | 768 |
| \((8,2,2,1)\) | 608 |
| \((8,2,2,2)\) | 304 |
| \((8,2,1,1)\) | 224 |
| \((8,2,1,2)\) | 128 |
| \((8,2,0,2)\) | 16 |

Consequently the total number of circular runs is precisely \(12\), \(13\), or \(14\), realized by \(1{,}008\), \(736\), or \(304\) cycles, respectively. No other run count or period profile is possible. This is a finite exact classification of the first sizable binary de Bruijn family, adjoining a uniform infinite-family short-period law.

## Assumptions and scope

A circular position is an element of \(\mathbb Z/(q^n)\mathbb Z\). For a start \(i\) and length \(L\), the corresponding factor consists of \(W_i,W_{i+1},\ldots,W_{i+L-1}\), with indices read cyclically. Its least period \(p\) is the smallest positive integer such that \(W_{i+j}=W_{i+j+p}\) for all \(0\le j<L-p\). It is a run if \(L\ge2p\) and neither extending the factor by one symbol on the left nor extending it by one on the right preserves period \(p\). Runs are counted as positioned intervals, not as distinct factor strings. Repetitions spanning a displayed linear cut are retained.

An interval of period \(p\) with \(p<q^n\) cannot have length \(n+p\) or more, since it would contain two equal length-\(n\) blocks at distinct circular starts separated by \(p\). Thus all considered runs are finite; a run of period \(p\) has length at most \(n+p-1\). Since its length is at least \(2p\), necessarily \(p<n\). No artificial period exceeding the whole cycle is counted.

The infinite-family formula applies when \(2p+1\le n\), not for every period below \(n\). The order-five table concerns binary cycles and exact circular maximal repetitions, rather than the unrelated number of runs in a Burrows–Wheeler transform or runs in a cut linear string.

## Proof

**1. Local primitive-square criterion.** A word \(u\) of length \(p\) is primitive when it is not an integer power of a shorter word. Its square \(uu\) has least period exactly \(p\): if it also had a smaller period \(r\), the Fine–Wilf periodicity lemma would make \(\gcd(p,r)\) a period, because the square length \(2p\) is at least \(p+r-\gcd(p,r)\). This would make \(u\) a proper power, a contradiction. Conversely, if a factor of length \(2p\) has least period \(p\), its first \(p\) symbols form a primitive word.

A circular run of least period \(p\) begins precisely at an occurrence of a length-\((2p+1)\) word \(a uu\), where \(u\) is primitive of length \(p\) and \(a\) differs from the last letter of \(u\). The occurrence is located at the first symbol of \(u\), not at \(a\). Indeed, this condition gives a least-period-\(p\) square which cannot extend left. Extending it right as long as period \(p\) remains valid produces exactly one maximal run; this process terminates by the de Bruijn uniqueness bound in the preceding section. Conversely, every run contains its first \(2p\) letters as such a primitive square, and the preceding letter differs from the period-\(p\) continuation. Both directions preserve the positioned starting point, so the correspondence is bijective.

**2. Universal short-period count.** Every prescribed word of length \(t\le n\) occurs exactly \(q^{n-t}\) times as a circular factor of a de Bruijn cycle of order \(n\), since the \(n\)-factors beginning with it are distinct and exhaust its \(q^{n-t}\) completions. There are \(P_q(p)\) primitive words of length \(p\); Möbius inversion of the identity that every length-\(p\) word is a power of a unique primitive root gives \(P_q(p)=\sum_{d\mid p}\mu(d)q^{p/d}\). For each primitive \(u\), exactly \(q-1\) preceding letters differ from its final symbol. When \(2p+1\le n\), the bijection from part 1 and uniform short-factor frequencies yield \((q-1)P_q(p)q^{n-2p-1}\) runs, proving the first formula.

**3. Exact shorter lengths.** Fix \(2p\le L\le n-2\). A period-\(p\) run of exact length \(L\) is detected by the \((L+2)\)-letter factor consisting of the run, preceded and followed by one letter. Its interior is the first \(L\) letters of the infinite periodic repetition of a primitive word \(u\) of length \(p\). For maximality, the preceding and following letters must each differ from their respective period-\(p\) continuations. These are independent choices of \(q-1\) symbols, hence there are \((q-1)^2P_q(p)\) detecting words. Each appears \(q^{n-L-2}\) times, giving the stated length formula. Summing this geometric progression over \(L=2p,\ldots,n-2\) gives \((q-1)P_q(p)(q^{n-2p-1}-1)\). Subtraction from the total in part 2 leaves exactly \((q-1)P_q(p)\) runs of length at least \(n-1\); this includes the empty-sum boundary \(n=2p+1\).

**4. Exhaustive, bijective order-five classification.** Write a five-bit state uniquely as \((b,s)\), where \(b\in\{0,1\}\) is its first bit and \(s\in\{0,\ldots,15\}\) is its final four-bit suffix. In any de Bruijn cycle the map advancing a five-bit window is a permutation, so states \((0,s)\) and \((1,s)\), whose successors share the same four-bit prefix, must append different bits. Consequently there is a unique Boolean function \(g:\{0,\ldots,15\}\to\{0,1\}\) for which the appended bit in state \((b,s)\) is \(b\oplus g(s)\). Conversely each of the \(2^{16}\) such functions defines a permutation of the 32 states. It gives a de Bruijn cycle exactly when the orbit of the all-zero five-bit state has length 32. Each cyclic de Bruijn word has exactly one occurrence of the five-zero block, hence this fixes a canonical origin and the feedback function uniquely. It follows that exhaustive testing of these \(65{,}536\) functions gives a bijective census with no rotation overcounting.

For each valid cycle, any run period is at most four by the uniqueness bound. For each \(p\in\{1,2,3,4\}\), form the circular equality vector \(E_p(i)=[W_i=W_{i+p}]\). Maximal consecutive one-blocks of length at least \(p\) correspond to maximal period-\(p\) factors. An explicit test that no smaller period exists retains precisely the runs of least period \(p\). The complete 65,536-function enumeration yields exactly 2,048 valid cycles and the six profile counts stated in the Finding. Periods one and two independently agree with the formulas in part 2: \(P_2(1)=P_2(2)=2\), giving \(R_{5,1}=8\) and \(R_{5,2}=2\).

For a second enumeration, treat each five-bit word as a directed edge between its first and last four-bit words in the order-four de Bruijn digraph. For every possible ordering of the two outgoing edges at each of its sixteen vertices, Hierholzer's algorithm produces a 32-edge Euler circuit. Taking the first bit of each successive edge and rotating to the unique five-zero window yields 2,048 distinct cycles, *identical as a set* to the valid feedback cycles. Independently, direct testing of all factor intervals of lengths 2 through 8, their least periods, and both extension boundaries reproduces every run located by the equality vectors, and therefore every listed count. The upper length 8 is exact since every order-five run has \(L\le n+p-1\le8\). All algorithms and asserted totals are in `checker.py`.

## Verification

Run `python3 checker.py` with a standard Python 3 interpreter. A successful execution prints `VERIFY_OK` after checking both independent cycle enumerations, all run sets, the six-profile table, total-count table, the period–length totals, and small binary/ternary de Bruijn instances against the universal formula. The two cycle enumerations both return 2,048 equal canonical strings, and the period-equality and direct-interval detectors agree on every one of those strings.

The aggregate positioned run totals by (least period, length), summed over all 2,048 cycles, are: \((1,2):8192\), \((1,3):4096\), \((1,5):4096\), \((2,4):1536\), \((2,5):1024\), \((2,6):1536\), \((3,6):1792\), \((3,7):1920\), \((4,8):1728\). Their sum is 25,920. The finite table is an exhaustive computation with a mathematically justified finite search space, not a claimed consequence of sampling; the infinite-family law is a symbolic proof, not an extrapolation of these tests.

## Relationship to prior work

Bannai, I, Inenaga, Nakashima, Takeda and Tsuruta's 2014 preprint on the runs theorem supplies the classical maximal-periodicity definition and a global bound for ordinary linear strings; it does not tabulate circular runs of de Bruijn cycles or force the six order-five profiles. Ilie, Yu and Zhang (2004), Section 7, establish a lower bound for a different invariant, *repetition complexity* of de Bruijn words; their Theorem 17 is not a count of positioned maximal runs. Fredricksen's 1982 survey describes full-cycle shift-register generation, rather than exact period-resolved run multiplicities. The familiar uniform count of shorter de Bruijn factors makes the first universal formula accessible by the primitive-square bijection; its simplicity should not be confused with a new general upper bound for arbitrary words. The distinctive exhaustive result is the precise distribution at the first boundary where period-three and period-four run counts can vary.

No matching exact order-five circular-run table was found in the inspected sources or targeted bibliographic searches. This absence is not proof of historical priority, and full-text coverage of some older sequence-generation literature was incomplete.

## Limitations

The distribution \((1008,736,304)\) concerns all circular runs of binary order-five cycles; it is not a universal distribution at other orders or alphabet sizes. The closed-form law applies only to periods satisfying \(2p+1\le n\), and the exact length formula only to lengths \(L\le n-2\). It does not determine individual counts in the nonrigid long-period region for general \(n\). No independent mathematical audit or all-literature priority certification has been performed.

## References

1. H. Bannai, T. I, S. Inenaga, Y. Nakashima, M. Takeda and K. Tsuruta, *The “Runs” Theorem*, arXiv:1406.0263, first posted 2014-06-02, https://arxiv.org/abs/1406.0263 (full public text inspected).
2. L. Ilie, S. Yu and K. Zhang, *Word Complexity and Repetitions in Words*, International Journal of Foundations of Computer Science 15 (2004), 41–55, https://doi.org/10.1142/S0129054104002297 and author manuscript https://www.csd.uwo.ca/~ilie/IJFCS04.pdf (relevant de Bruijn section inspected).
3. H. Fredricksen, *A Survey of Full Length Nonlinear Shift Register Cycle Algorithms*, SIAM Review 24 (1982), 195–221, https://doi.org/10.1137/1024041 (abstract consulted; full text not inspected).
4. N. G. de Bruijn, *A Combinatorial Problem*, Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764 (historical definition and enumeration).
5. N. Fine and H. Wilf, *Uniqueness Theorems for Periodic Functions*, Proceedings of the American Mathematical Society 16 (1965), 109–114 (periodicity lemma).
