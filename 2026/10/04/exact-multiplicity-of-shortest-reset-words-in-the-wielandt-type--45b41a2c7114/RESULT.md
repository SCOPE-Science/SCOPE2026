# Exact multiplicity of shortest reset words in the Wielandt-type family

## Finding
Let \(2\le p<q\) be coprime and set \(s=q-p+1\). Consider the binary automaton \(W(q,q,p)\) on \(Q=\mathbb Z/q\mathbb Z\) with
\[
b(i)=i+1,\qquad a(i)=i+1\text{ for }i\ne0,\qquad a(0)=s,
\]
where additions in state labels are modulo \(q\). Its reset threshold is
\[
L=(p-1)(q-1)+q-p=pq-2p+1.
\]
The number of reset words of this minimum length is exactly
\[
2^{(p-1)(q-3)}.
\]
Every shortest reset word sends all states to \(s\).

## Assumptions and scope
The parameters satisfy \(2\le p<q\) and \(\gcd(p,q)=1\). The automaton is exactly the \(n=q\) Wielandt-type family introduced by Gusev and Pribavkina. The statement concerns the multiplicity of shortest reset words, not the number of minimal reset words under factor containment and not longer reset words.

## Proof
The cited construction has \(b\) equal to the cyclic shift and \(a\) differing from \(b\) only at state \(0\). The source proves that the reset threshold is \(L\) and that every shortest reset word resets to \(s=q-p+1\).

Take a shortest reset word and read it backwards from the singleton \(T_0=\{s\}\). After \(t\) reversed letters, let \(T_t\) be the full preimage of \(\{s\}\) under the processed suffix, and rotate coordinates by time:
\[
R_t=T_t+t\pmod q.
\]
Put \(d=q-p\). At reversed step \(t+1\), write \(j=t+1\pmod q\). A preimage under \(b\) is just a backward cyclic shift, so it leaves \(R_t\) unchanged. A preimage under \(a\) has the same effect at every rotated coordinate except \(j\), and at \(j\) it copies the membership bit at \(j+d\). Thus \(b\) is a no-op on \(R_t\), whereas \(a\) performs the scheduled Boolean update
\[
1_{R}(j)\leftarrow 1_{R}(j+d).
\]

The dependency map \(j\mapsto j+d\) is one cycle because \(\gcd(d,q)=1\). Starting with \(R_0=\{s\}\), write
\[
r_0=s,\qquad r_m=s-m d\equiv s+mp\pmod q.
\]
A state \(r_m\) with \(m\ge1\) can become present only after \(r_{m-1}\) is present and the schedule visits \(r_m\). The earliest such visits occur at
\[
\tau_m=1+(m-1)p,\qquad 1\le m\le q-1,
\]
because \(\tau_m\equiv r_m\pmod q\) and successive visits are separated by \(p\) steps. If any of these copies is skipped, its next opportunity is \(q\) steps later, which is later than the next required copy because \(q>p\); consequently the final state \(r_{q-1}\) cannot be present by \(\tau_{q-1}=1+(q-2)p=L\). Hence each of the \(q-1\) steps \(\tau_m\) forces the letter \(a\).

Before the last copy, the only present state whose dependency successor is absent is the initial endpoint \(s\): its successor \(s+d\) is precisely \(r_{q-1}\), the last state to be created. Therefore every scheduled visit to \(s\) before time \(L\) forces \(b\), since \(a\) would erase \(s\). These visits are
\[
s,\ s+q,\ldots,\ s+(p-2)q,
\]
so there are exactly \(p-1\) forced \(b\)-positions. At every remaining step, the two compared membership bits agree, and \(a\) and \(b\) have exactly the same preimage action. Such positions are independent binary choices.

The number of free positions is therefore
\[
L-(q-1)-(p-1)=(p-1)(q-3),
\]
which gives exactly \(2^{(p-1)(q-3)}\) shortest reset words.

## Verification
The included verifier performs exact forward power-automaton breadth-first search for every coprime pair \(2\le p<q\le13\). For each pair it checks the published reset threshold, the unique reset target \(s\), and the exact count \(2^{(p-1)(q-3)}\). It also replays the symbolic rotating-preimage schedule for every coprime pair with \(q\le100\), checking all forced-copy times and the counts of forced and free positions. The recorded output is `VERIFY_OK exhaustive_power_cases=45 symbolic_q_max=100`.

## Relationship to prior work
Gusev and Pribavkina define \(W(q,q,p)\), prove that every shortest reset word ends at \(q-p+1\), prove the reset threshold \(L=(p-1)(q-1)+q-p\), and exhibit one shortest reset word. Their theorem does not count all shortest reset words. The exact multiplicity above refines that extremal-length result by describing the branching left after all critical reverse-preimage updates are forced.

A separate algorithmic paper by Kisielewicz, Kowalski, and Szykuła develops exact methods for finding shortest reset words in general automata; it provides computational context but does not state this family-specific multiplicity formula. Searches for the exact formula, the family name together with shortest-word multiplicity, and equivalent minimal-reset-word language terminology did not identify a stronger published statement covering the claim.

## Limitations
The proof uses the special two-edge structure of \(W(q,q,p)\) with \(n=q\); it does not claim the same multiplicity for the more general \(W(n,q,p)\) family with \(n>q\), nor for the Dulmage--Mendelsohn-type families. The originality assessment is literature-based rather than exhaustive over every unpublished source.

## References
1. V. V. Gusev and E. V. Pribavkina, *Reset thresholds of automata with two cycle lengths*, arXiv:1403.3992v1, first posted 2014-03-17; later in *Implementation and Application of Automata*, LNCS 8587. The definition of \(W(q,q,p)\), the reset target, the threshold theorem, and one optimal word appear in Section 2.
2. A. Kisielewicz, J. Kowalski, and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization 29 (2015), 88--124; published online 2013-11-17.
