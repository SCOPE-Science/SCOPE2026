# Independent mathematical audit

## correctness

PASS

Fresh independently coded exact-state recurrence on four suffix-bit states and all 256 observed triple masks starts once from each two-bit word and appends both bits. For n=3..50, the 256 counts sum exactly to 2^n. It separately found at n=13: c(full)=934 versus two masks 0x7f,0xfe at 989; at n=14: full=2632 versus largest proper=2218; and strict full maximum every n=14..50. For n>=51, any missing triple e forces avoidance in t=floor(n/3) independent nonoverlapping triples, so each proper fiber <=2^n(7/8)^t, while full fiber >=2^n[1-8(7/8)^t]; strict since 9(7/8)^17=2093674625884863/2251799813685248<1. The 256-term inclusion-exclusion with four-state forbidden-edge matrices independently follows. Finite checks certify only specified finite range; tail is proven by exact rational bound.

## originality

PASS

Set-of-k-substrings is a well-studied equivalence relation. The closest published full HTML source Bernardini et al. states and studies shortest equivalent strings and efficient listing, explicitly distinguishing general set-based counting as open. Its broader model does not provide this sharp *fixed-length* modal fiber comparison, while multiplicity-aware k-abelian and multiset-spectrum problems are distinct. Search of Resultary found related but non-covering binary reconstruction enumerations. Older 1995 exact source content is only abstract-available, leaving bounded priority risk.

## value

PASS

The fixed-length presence-only observation model has meaningful worst-case ambiguity. All eight probes positive becomes uniquely worst only from n=14; the n=13 two-mask counterexample and exact all-length fiber count supply concrete sharp guidance for reconstruction and privacy analyses. This is a natural finite-automaton structural threshold, not an arbitrary code size census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
