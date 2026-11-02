# Scientific review

## Correctness — PASS

The proof is self-contained. The reverse-complement orbit count is \(36\) for binary six-mers. A five-bit potential with precisely five values equal to \(2\), five equal to \(0\), and the remaining values equal to \(1\) has nonnegative, reverse-complement-invariant edge costs. Direct enumeration of the eight fixed words yields cost sum \(18\), the full directed de Bruijn edge sum is \(64\), and the resulting orbit-weight sum is \(41\). Telescoping bounds it above by the number of windows plus \(2\), forcing at least \(39\) windows. The displayed \(44\)-bit word has exactly those \(39\) windows and hits all classes. The standalone source code checks every finite fact, with independent string- and integer-level orbit implementations. The lower bound is unrestricted in word length.

## Originality — PASS, qualified

Orenstein and Shamir (2013), full article Sections 3.1–3.3.2 and Tables 1–2, already solve the general optimal reverse-complement coverage problem algorithmically and report a table for four-letter DNA, not the binary case. The new claim is not the invention of reverse-complement coverage or of exact optimization algorithms. The inspected primary paper does not state the binary six-mer optimum, a sparse five-bit potential certificate, or the first even-order failure of the elementary class-count bound. Medvedev and collaborators' 2007/2009 bidirected postman methods are more general optimization context; their available abstracts do not resolve this specific comparison. Searches of relevant mathematical records, web literature and accessible previous claims found no matching theorem. Risks include an unindexed binary specialization, an incidental calculation in an algorithm implementation, and non-accessible full text of the earlier bidirected-graph work.

## Value — PASS

Orenstein and Shamir explicitly motivate minimization of reverse-complement-universal probes. The orbit count gives the natural information-theoretic lower bound, but the first instance at which it ceases to be attainable is a meaningful boundary for this model. Here the deficit is sharply three windows, supported by a short human-checkable dual certificate rather than merely a shortest-path output. Its pattern gives a reusable way to test other finite reverse-complement covering instances; no full all-order formula is claimed.

## Residual limitations

The exact optimization concerns a two-letter alphabet and linear contiguous windows at orders \(2,4,6\). The four-letter DNA problem and higher orders are not classified. Priority remains provisional pending a specialist reading of all relevant historical sources. Numerical code replay is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
