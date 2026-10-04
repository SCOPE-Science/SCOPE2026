# First break in the period-\(30\) record-multiple pattern

## Finding
Let \(R\) be the set of record values of the permutation \(f_3\) introduced by Basistha and Ionascu. The records satisfy
\[
r_{j+1}=r_j-1+\ell(r_j-1),
\]
where \(\ell(N)\) denotes the least prime that does not divide \(N\).

Put
\[
P=23\#=2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23
=223092870.
\]
Then
\[
25+30m\in R
\]
for every integer
\[
0\le m<\frac{P}{30}=7436429,
\]
but
\[
P+25=223092895\notin R.
\]

Therefore the arithmetic progression of record multiples
\[
25,55,85,115,\ldots
\]
continues without a missing term through
\[
P-5=223092865
\]
and fails for the first time at
\[
223092895.
\]

## Assumptions and scope
The source calls a value of \(f_3\) at a turning point a record. Its record sequence is the sequence whose next term is the least integer larger than the current record and coprime to one less than the current record; equivalently it is OEIS A261271.

The theorem concerns only the residue progression \(25\pmod{30}\), motivated by the source's explicit observation that the first record multiples of \(5\) are
\[
25,55,85,115,145,175,205,\ldots
\]
and that consecutive displayed terms differ by \(30\).

No claim is made that all record multiples of \(5\) are classified after the first failure.

## Proof
Let
\[
r<r'
\]
be consecutive records. By the recurrence,
\[
r'=r-1+\ell(r-1),
\]
so
\[
r'-r=\ell(r-1)-1.
\]

Take an integer
\[
x\equiv25\pmod{30},
\qquad
25\le x<P+25.
\]
Suppose for contradiction that \(x\notin R\). Then \(x\) lies strictly between consecutive records \(r<r'\).

If
\[
\ell(r-1)=3,
\]
then \(r'-r=2\). Since these records are odd, there is no odd integer strictly between them.

If
\[
\ell(r-1)=5,
\]
then \(r'-r=4\), and the only odd integer strictly between the two odd records is \(r+2\). The condition \(\ell(r-1)=5\) gives
\[
2\mid r-1,\qquad 3\mid r-1,
\]
so
\[
r\equiv1\pmod6.
\]
But \(x=r+2\equiv25\pmod{30}\) would imply
\[
r\equiv23\pmod{30},
\]
hence \(r\equiv5\pmod6\), a contradiction.

Now assume
\[
\ell(r-1)\ge7.
\]
Then \(2,3,5\) divide \(r-1\), so
\[
r\equiv1\pmod{30}.
\]
Because \(x\equiv25\pmod{30}\) and \(x>r\),
\[
x-r\ge24.
\]
The strict inequality \(x<r'\) gives
\[
\ell(r-1)-1>24,
\]
hence
\[
\ell(r-1)\ge29.
\]
Therefore every prime below \(29\),
\[
2,3,5,7,11,13,17,19,23,
\]
divides \(r-1\). Thus
\[
P\mid r-1,
\]
so
\[
r\ge P+1
\]
and
\[
x\ge r+24\ge P+25,
\]
contrary to the assumed bound. Hence every \(x\equiv25\pmod{30}\) below \(P+25\) is a record.

It remains to show that \(P+25\) is not a record. First, \(P+1\) is a record. Suppose otherwise and let \(r<P+1\) be the largest preceding record. Because \(P+1\) is skipped, it is not coprime to \(r-1\). Any common prime divisor of \(P+1\) and \(r-1\) is at least \(29\), since every prime at most \(23\) divides \(P\) and hence cannot divide \(P+1\). Therefore
\[
P+1-(r-1)\ge29.
\]
Since \(r-1<P\), at least one prime
\[
q\in\{2,3,5,7,11,13,17,19,23\}
\]
does not divide \(r-1\). Then
\[
\gcd(r-1,r-1+q)=1,
\]
while
\[
r<r-1+q<P+1,
\]
contradicting the maximality of \(r\). Thus \(P+1\) is a record.

At \(r=P+1\), the number \(r-1=P\) is divisible by every prime through \(23\) and is not divisible by \(29\). Hence
\[
\ell(P)=29,
\]
so the next record is
\[
P+29.
\]
Every integer strictly between \(P+1\) and \(P+29\), in particular
\[
P+25=223092895,
\]
is therefore not a record. Since
\[
P+25=25+30\frac{P}{30},
\]
this is exactly the first failed term of the progression.

## Verification
The accompanying `verify.py` reconstructs the record recurrence from the least-prime-not-dividing rule and checks the modular cases in the proof.

It verifies
\[
P=223092870,\qquad \frac{P}{30}=7436429,
\]
checks that the local recurrence at \(P+1\) jumps directly to \(P+29\), and confirms that \(P+25\) lies strictly inside that gap.

As a regression check, it also generates all records below \(10^6\) and confirms that every integer congruent to \(25\pmod{30}\) in that range is a record.

The finite regression is not the proof of the cutoff. The cutoff follows from the exact gap argument above.

## Relationship to prior work
Basistha and Ionascu ask for a useful description of the composite records and explicitly list the first record multiples of \(5\):
\[
25,55,85,115,145,175,205,235,265,295,325,355,385,415,445,475,\ldots
\]
They note that consecutive displayed terms differ by \(30\), but do not give a first failure or an all-range theorem for that progression.

Their primorial results prove broad families of records around primorials. The proof here instead identifies the first possible record gap long enough to swallow a number congruent to \(25\pmod{30}\), and shows that the obstruction occurs exactly at the \(23\)-primorial.

OEIS A261271 gives the record recurrence and initial values, while OEIS A085229 records the underlying permutation and references the same paper. Neither inspected entry states the cutoff
\[
223092895
\]
or the first-failure theorem.

Targeted searches for the exact cutoff, the \(23\#+25\) formulation, and the period-\(30\) record-multiple pattern did not locate a prior statement of this result.

## Limitations
The theorem does not describe the record multiples of \(5\) after the first failure, nor does it classify record multiples of other primes.

Literature non-detection cannot rule out an unindexed or unpublished equivalent observation.

## References
1. Amit Kumar Basistha and Eugen J. Ionascu, “A special sequence and primorial numbers,” arXiv:2302.02838v1, first posted 6 February 2023; MSC \(11A05\).
2. OEIS A261271, the record recurrence \(a(n)=a(n-1)-1+p\) with \(p\) the least prime not dividing \(a(n-1)-1\).
3. OEIS A085229, the underlying permutation \(f_3\).
