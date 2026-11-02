# Scientific review: Exact GCDs of consecutive cubic Fibonacci windows

## Correctness — PASS

The theorem is a quantified closed formula for the GCD of all shifted sums of \(k\) consecutive Fibonacci cubes, for each integer \(k\ge1\). The proof derives the characteristic polynomial \((t^2-4t-1)(t^2+t-1)\) for the cubes, reduces the infinite GCD to the GCD of the initial window and four consecutive differences, and expresses the latter using \(x=F_k\) and \(y=F_{k+1}\). Standard Cassini/addition identities give the common factor \(H(k)\), and precise valuations at \(2\) and \(3\) establish the only exceptional factors. The exact telescoper \(P(Y,X+Y)-P(X,Y)=2X^3\) then determines the remaining halving rule. The GCD theorem is proved for every positive \(k\), not merely those tested in code.

The accompanying standalone Python 3 checker was executed; it compared 8,400 cubic-window sums for \(1\le k\le300\) from two disjoint sets of 14 initial offsets, independently checked the reduced difference GCDs, and validated the integer recurrence and telescoping identity. Finite arithmetic checks do not establish the infinite claim on their own.

## Originality — PASS within the inspected evidence

The closest primary source is aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626, first publicly submitted 2022-04-26. Its square-power theorems and cubic Question 6.1 were inspected at their proof and open-problem sections, including the relevant full-text PDF pages. The posed cubic extension is a question/conjecture rather than an established general cubic-GCD theorem. Its printed conjectural parity adjustment does not agree with directly computed examples \(k=2\) and \(k=6\); this manuscript does not use that conjecture as a premise.

D. Guyer and aBa Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262, establishes related first-power GCD formulas but not cubic windows. K. Adegoke, *Factored closed-form expressions for the sums of cubes of Fibonacci and Lucas numbers*, arXiv:1706.08469, treats cubic sums, not the simultaneous GCD across every shift. The related full texts were inspected, and targeted searches for equivalent shifted-window, higher-power, order-four-recurrence, and prime-valuation formulations did not uncover a proof of the precise theorem. The lack of a retrieved result is not evidence of a complete priority census; an unindexed independent solution remains possible.

## Mathematical value — PASS

The work resolves a natural higher-power extension explicitly proposed in a primary number-theory paper. It classifies the infinite-window GCD for every length, including odd windows, distinguishes the \(8\mid k\) factor of three from the \(6\mid k\) halving, and gives the result directly in standard Fibonacci and Lucas numbers. The reduction to four consecutive cubic differences plus an exact polynomial telescoper also gives a reusable elementary method for recurrence-window divisibility questions. This is not merely a finite numerical table or a restatement of the square-power theorem.

## Limits and evidence

The general proof uses classical identities whose hypotheses and parity cases are detailed in RESULT.md. No claim is made for arbitrary Gibonacci starts, Lucas cubes, or general powers. The verifier is ordinary reproducibility code, not independent certification; possible earlier implicit results remain a bibliographic limitation.

Self-review: passed. Independent audit: not yet performed.
