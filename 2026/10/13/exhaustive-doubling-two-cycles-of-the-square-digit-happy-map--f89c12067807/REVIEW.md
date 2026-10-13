# Review

## Correctness
PASS. Writing \(X=ab+c\), the no-carry case for doubling gives \(S_b(2X)=4S_b(X)=8X\), contradicting \(S_b(2X)=X\). Thus a carry is forced. The two exact cycle equations then reduce, after eliminating \(c\), to
\[
(b^2+1)(5a-b+3)(13a-b+5)=0.
\]
The branch \(b=13a+5\) yields \(c=5a+2\), which contradicts the required carry. The surviving branch gives \(b=5a+3\), \(c=3a+2\), and the converse is checked directly. Digit bounds and the two-digit hypotheses are explicitly retained throughout.

## Originality
PASS. The closest source is the 2025 paper of Goedhart, Gurtas, and Harris: it gives exactly the positive family and notes that the larger cycle member is twice the smaller, but presents this as a formula generating examples rather than an exhaustive classification. Earlier cycle-count and finite-base sources record cycle data, including the base-\(8\) and base-\(13\) examples, without stating the converse. Targeted statement-level searches for a two-digit doubling converse, the equations \(S_b(X)=2X\) and \(S_b(2X)=X\), and the \(5t+3\) family found no equivalent theorem.

The principal residual risk is incomplete access to the body of Hargreaves--Siksek (2010). Its accessible abstract emphasizes cycle bounds and fixed-point enumeration, not a two-cycle normal form.

## Value
PASS. The ratio-two family is singled out explicitly in the modern happy-function literature. Showing that its congruence \(b\equiv3\pmod5\) and digit pattern are forced converts a construction into a complete structural classification on a natural minimal digit stratum. The proof also identifies the carry as the rigidity mechanism and explains why the apparent second algebraic branch cannot occur.

Self-review: passed. Independent audit: not yet performed.
