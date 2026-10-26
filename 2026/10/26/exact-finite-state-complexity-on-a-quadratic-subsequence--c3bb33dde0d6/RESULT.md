# Exact finite-state complexity on a quadratic subsequence

## Finding

Let \(C(x)\) denote finite-state complexity under the standard encoding \(S_0\) of binary deterministic sequential transducers described in [1,2]. For every integer \(n\ge1\),
\[
C(0^n)\ge 2\sqrt{2n}+4.
\]
The bound is attained if and only if \(n=2a^2\) for an integer \(a\ge1\). Consequently,
\[
\boxed{C(0^{2a^2})=4a+4\qquad(a\ge1).}
\]

## Assumptions and scope

A transducer has \(s\ge1\) states and two outgoing transitions per state, one for each binary input symbol. Every transition has a finite binary output word. A description is a pair \((T,p)\), where \(p\in\{0,1\}^*\) and \(T(p)=x\); its length is the encoded transducer length plus \(|p|\). The standard encoding stores each transition output \(v\) in \(2|v|+2\) bits, before any non-self-loop target-state code. The claim concerns this fixed encoding, not arbitrary encodings of transducers.

## Proof

Fix a description \((T,p)\) of \(0^n\). Let \(s\) be the number of states, \(k=|p|\), and
\[
L=\sum_{e}|v_e|,
\]
where the sum runs over all \(2s\) transitions and \(v_e\) is the output word on transition \(e\). The output encoding contributes \(2L+4s\) bits; target-state fields can only increase the encoded length. Thus
\[
|\sigma_T|+k\ge 2L+4s+k.
\]
Each input symbol produces at most \(\max_e|v_e|\le L\) output bits, so \(n=|T(p)|\le kL\). By the arithmetic-geometric mean inequality,
\[
2L+k\ge 2\sqrt{2Lk}\ge2\sqrt{2n}.
\]
Since \(s\ge1\), every description therefore has length at least \(2\sqrt{2n}+4\). Taking the minimum over all descriptions proves the lower bound.

Now let \(a\ge1\) and set \(n=2a^2\). Use a one-state transducer whose input-\(0\) self-loop outputs \(0^a\) and whose input-\(1\) self-loop outputs the empty word. On input \(p=0^{2a}\), it outputs \(0^{2a^2}\). The two self-loop output codes have lengths \(2a+2\) and \(2\), respectively, so the transducer encoding has length \(2a+4\). Including the input length gives
\[
C(0^{2a^2})\le (2a+4)+2a=4a+4.
\]
The lower bound at \(n=2a^2\) is \(2\sqrt{4a^2}+4=4a+4\), hence equality follows.

Finally, \(C(0^n)\) is an integer. Equality with \(2\sqrt{2n}+4\) forces \(2n\) to be a perfect square. Because \(2n\) is even, its square root must be even, say \(2a\); hence \(n=2a^2\). The construction above proves equality for every such \(n\), completing the classification of equality cases.

## Verification

The proof uses only the stated encoding-length formula and the fact that one input symbol can emit no more than the total output length stored across all transitions. It covers every finite-state transducer and every input description, including transducers with unreachable states. No finite search is used as a substitute for the universal lower bound. The explicit one-state construction verifies the upper bound on the equality subsequence.

## Relationship to prior work

Roblot’s thesis proves \(C(0^n)\in\Theta(\sqrt n)\) and gives coarser lower and upper estimates [1, Theorem 26, pp. 17–18]. Calude, Salomaa, and Roblot develop the standard encoding and study the state-size hierarchy [2]. The exact equality subsequence and the lower bound \(2\sqrt{2n}+4\) are stronger than the coarse \(\Theta(\sqrt n)\) statement; they are not implied by asymptotic order alone. The literature searches recorded with this result returned no directly matching published-finding corpus claim. This is a focused strengthening for the constant-word family, not a claim to resolve the full function \(C(0^n)\).

## Limitations

The result does not determine \(C(0^n)\) for general \(n\) outside the equality subsequence. It does not establish the asymptotic leading constant for all \(n\), nor does it transfer to a different transducer encoding without rechecking its length formula. A related 2011 journal treatment of finite-state complexity was not inspected in full; possible coverage there remains a literature-overlap risk.

## References

[1] Tania K. Roblot, *The Computation of Finite-State Complexity*, MSc thesis, University of Auckland, 2011, Theorem 26 and its proof, pp. 17–18.

[2] Cristian S. Calude, Kai Salomaa, and Tania K. Roblot, “Finite-State Complexity and the Size of Transducers,” *Electronic Proceedings in Theoretical Computer Science* 31 (2010), 38–47. arXiv:1008.1667, first submitted 10 August 2010. DOI: 10.4204/EPTCS.31.6.
