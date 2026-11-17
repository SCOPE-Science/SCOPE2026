# Independent mathematical audit

## correctness

PASS

From prescribed recurrence, f_n=q^n u_n with 3-periodic u_{3j+1}=1,u_{3j+2}=t,u_{3j+3}=−(t+1). General binomids equal q^{k(n−k)} t^{E2} (−t−1)^{E0}; E0≥0, E2≥−1, and E2=−1 forces k,n−k≥2, hence t|q⁴ suffices. [4,2]_f=−q⁴(t+1)/t gives necessity using gcd(t,t+1)=1. Index pair f4/f2=q²/t gives t|q² necessity, and m mod3 case analysis suffices. Independently checked 156 (q,t) pairs through n=12 by exact integer products, not only closed-form formula; inspected standalone artifacts/check.py but did not execute it unmodified.

## originality

PASS

The signed growing second-order cyclotomic family gives a negative answer to a clearly stated Shapiro question for ordinary binomid (not all-level pyramid) integrality. Prior repeated-root and eventually-periodic recurrence classifications exclude nonperiodic q^n cyclotomic roots; divisibility-only classifications cannot encompass the explicit nondivisible examples.

## value

PASS

Directly answers the open base-level version of the binomid-versus-divisibility second-order recurrence question with an infinite, unbounded, genuinely second-order family and sharp necessary-and-sufficient parameters. The q³ witness is neither a constant recurrence nor a cheap definitional substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
