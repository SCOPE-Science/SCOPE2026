# Review: Exact high-deficiency rank profile of Pribavkina's \(\widehat{\mathcal F}(k,u)\) automata

## Correctness
**PASS.** The transition rules admit a phase map modulo \(k\) on the nonzero states, and every nonzero transition advances phase by one. If a word reaches rank at most \(k-r\), at least \(r+1\) phases must be killed. Using the canonical representative of each phase, every killed phase forces a full occurrence of \(u\), and distinct killed phases force distinct start residues modulo \(k\). Unborderedness prevents overlap, so the selected occurrences are separated by at least \(k+1\), giving the lower bound \(k+r(k+1)\).

For the matching upper bound, the first copy of \(u\) merges the two states in every nonzero phase. The word \(u(au)^r\) then contains \(r+1\) displayed copies of \(u\) in distinct residue classes, so at most \(k-r-1\) nonzero phases survive and the total rank is at most \(k-r\). The lower bound forces equality. Exact power-automaton checks on all binary unbordered words through \(k=7\) and all ternary unbordered words through \(k=5\) returned `VERIFY_OK`.

Risk: the key proof obligation is that a killed canonical phase representative cannot reach the sink without a full aligned copy of \(u\). This is secured by the unique predecessor chain \(1\to2\to\cdots\to k\to0\) for sink entry. The computation is not used as an infinite proof.

## Originality
**PASS.** The defining Pribavkina paper was read in full around its incomplete-word lemmas and automaton construction. It proves the shortest reset word \(k^2+k-1\), corresponding only to the endpoint \(r=k-1\), and does not state an intermediate transformation-rank profile. Volkov's later survey was checked both in its general rank discussion and in its automata-with-zero section; it records reset-threshold results and cites Pribavkina's series but does not give this formula.

published-finding corpus searches under the original automaton notation, semi-flower terminology, incomplete-set terminology, rank compression, and incompletable-word language found no equivalent claim. The closest exact synchronization records concern the Černý avoiding profile and a different finite one-cluster census, neither of which implies the present statement.

Residual risk: an older unindexed treatment of incomplete sets or transformation rank may contain the same formula under different language. No decisive unresolved comparison remains among the sources inspected.

## Value
**PASS.** The known literature singles out this family because of its quadratic reset threshold. Determining every high-deficiency threshold from rank \(k\) down to rank \(1\) explains how that endpoint is accumulated and gives uniform structural information for all unbordered defining words and all finite alphabets. The phase/nonoverlap mechanism is mathematically motivated by the original incomplete-word construction and is not a routine recomputation of a finite table.

The result is deliberately limited to the high-deficiency half of the profile; finite checks show that the low-deficiency half can depend on the letter pattern of \(u\).

## Closest literature and limitations
The closest source is Pribavkina's 2009 preprint and 2011 journal paper defining \(\widehat{\mathcal F}(k,u)\) and proving its reset threshold. Volkov's 2022 survey supplies broader transformation-rank and sink-state context. The theorem does not classify thresholds above rank \(k\), and originality retains the ordinary risk of an older equivalent result under different terminology.

Same-model review: passed. Independent audit: not yet performed.
