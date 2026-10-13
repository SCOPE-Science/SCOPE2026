# Scientific review: minimum-row ternary Armstrong relations

## Correctness — PASS
The general lower bound uses the injection from column-pair requirements to distinct row-pair witnesses. For equal row and column counts, every row pair must witness exactly one column pair; the partition-mask search therefore excludes no possible equality case. The \(4\), \(40\) and \(121\) canonical column sets at row counts \(3\), \(5\) and \(6\) are exhaustive under individual symbol relabeling. Both Python and independently coded C++ exhaust all single-edge-overlap choices while forbidding triple-use of any row pair; both obtain zero completed diagonal families. Explicit rows achieve the upper bounds, confirmed by direct pairwise tests. The previously known \(f(3,3)=7\) theorem excludes larger attribute counts. The supplied source files can be rerun without private dependencies.

## Originality — PASS, with risks
The exact minimum-row profile is not provided by the inspected foundational Armstrong-relation treatment, the bounded-alphabet coding paper, or the full-length Chee–Zhang–Zhang paper. The known seven-row, seven-column construction and the bound on the number of attributes are properly credited; the new claim is the **minimum row count at every admissible ternary three-key length**, especially strictness at five and six columns. The closest numerical bound \(m\ge n\) does not give either strict inequality. Search did not locate a table or theorem giving this full profile under equivalent column-partition language. A missing specialist computation could overlap, so bibliographic originality is not independently certified.

## Value — PASS
For a database schema in which every triple of attributes is a minimal key, finding the least number of records is the natural representation-size problem. This complete small-alphabet function reveals nontrivial extra-record requirements at five and six columns, while attaining the counting bound at four and seven. Explicit tables and independent exhaustive checkers make the result a reproducible test instance for bounded-domain relational dependencies rather than a renamed existing upper bound.

## Limits
The searches establish exact facts only for the stated finite cases. The impossibility of eight or more columns is cited from prior literature, not reproved. Independent literature review, mathematical audit and formal certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
