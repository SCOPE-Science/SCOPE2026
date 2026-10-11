# Independent mathematical audit

## correctness

PASS

Hébrard/arch factorization gives the universality index as the number of complete arches. Over a binary alphabet an arch has the unique form \(a^r\bar a\) with \(r\ge1\), so its ordinary generating function is \(A(z)=2z^2/(1-z)\); the terminal remainder is empty or a positive unary word, with \(R(z)=(1+z)/(1-z)\). Unique arch factorization therefore gives \(F(z,u)=R(z)/(1-uA(z))=(1+z)/(1-z-2uz^2)\). Coefficient extraction yields the stated \(N_{n,j}\) law and, after appending an arbitrary suffix after the \(k\)-th arch, the stated formula for the number of \(k\)-universal binary words. Differentiating \(F\) at \(u=1\) gives the claimed expectation and variance. An independent exhaustive enumeration of all binary words through length 10 matched every distribution coefficient and both moment formulas exactly.

## originality

PASS

Adamson gives an \(O(nk\sigma)\) recursive counting algorithm for arbitrary alphabet size and explicitly asks for a general formula for the number of fixed-length \(k\)-subsequence-universal words. The audited result solves the complete binary distribution, not merely the threshold count: it gives a bivariate rational generating function, exact level counts, the exact \(k\)-universal count, and moments of the universality index. The binary Simon-congruence literature characterizes congruence classes but does not state this arch-count distribution. Targeted exact-formula and generating-function searches found no prior theorem implying these formulas.

## value

PASS

This is a natural complete classification of the binary case of an explicitly posed counting problem, including the full universality-index law rather than a single count. The exact moments and rational bivariate generating function are reusable analytic summaries and go materially beyond a routine decision test or finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
