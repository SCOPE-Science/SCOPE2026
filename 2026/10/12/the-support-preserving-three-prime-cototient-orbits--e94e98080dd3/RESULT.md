# The support-preserving three-prime cototient orbits

## Finding

Let \(\varphi\) be Euler's totient function, let \(T(n)=n-\varphi(n)\) for integers \(n>1\), and let \(H(n)\) denote the number of applications of \(T\) required to reach \(1\). Let \(q>3\) be a prime and let \(a,b,c\) be positive integers. The following conditions are equivalent:

1. Every positive iterate of \(T\), starting at \(2^a3^bq^c\) and ending at \(1\), has all prime factors in \(\{2,3,q\}\).
2. The first iterate \(T(2^a3^bq^c)\) has all prime factors in \(\{2,3,q\}\).
3. There is an integer \(h\ge3\) such that \(2q+1=3^h\).

When these conditions hold, the entire orbit and its length are explicit. With \(d=b+(h-1)c\), its successive states are

\[
T^j(2^a3^bq^c)=2^a3^{b+(h-1)j}q^{c-j}\quad(0\le j\le c),
\]
\[
T^{c+j}(2^a3^bq^c)=2^{a+j}3^{d-j}\quad(0\le j\le d),
\]
\[
T^{c+d+t}(2^a3^bq^c)=2^{a+d-t}\quad(0\le t\le a+d).
\]
Consequently,
\[
\boxed{H(2^a3^bq^c)=a+2b+(2h-1)c.}
\]
In the corresponding NONTOTIENT game, which has the unique move \(n\mapsto T(n)\), the Sprague–Grundy value is
\[
\boxed{\operatorname{SG}(2^a3^bq^c)\equiv a+c\pmod2.}
\]
For example, \(q=13\) gives \(h=3\), and \(q=1093\) gives \(h=7\); both are prime. For \(q=13\), the initial position \(2\cdot3\cdot13=78\) has orbit length \(8\), while \(4\cdot3\cdot13=156\) has length \(9\).

## Assumptions and scope

The prime \(q>3\) is arbitrary, as are all positive exponent triples \((a,b,c)\). The theorem characterizes precisely those \(q\) for which a full cototient orbit starting with exactly the prime support \(\{2,3,q\}\) remains within that support. No assertion is made about analogous invariant supports involving different distinguished primes, or about how many primes \((3^h-1)/2\) exist. Iteration stops at \(1\); the extension \(T(1)=0\) is not included.

## Proof

Since \(a,b,c\ge1\), multiplicativity gives
\[
\varphi(2^a3^bq^c)=2^a3^{b-1}(q-1)q^{c-1},
\]
so
\[
T(2^a3^bq^c)=2^a3^{b-1}q^{c-1}(2q+1).\tag{1}
\]
The factor \(2q+1\) is odd and relatively prime to \(q\). Therefore its prime divisors belong to \(\{2,3,q\}\) if and only if it is a positive power of \(3\). Since \(q>3\), the power is \(3^h\) with \(h\ge3\). Thus condition 2 implies condition 3. Conversely, condition 1 implies condition 2.

If \(2q+1=3^h\), equation (1) reduces to
\[
T(2^a3^bq^c)=2^a3^{b+h-1}q^{c-1}.
\]
This identity can be iterated while a positive power of \(q\) remains, giving the first displayed orbit segment; throughout it the exponent of \(3\) remains positive. At the end of this segment the state is \(2^a3^d\) with \(d=b+(h-1)c\). For all positive integers \(u,v\), a second totient computation gives
\[
T(2^u3^v)=2^{u+1}3^{v-1}.
\]
Iterating this identity \(d\) times reaches \(2^{a+d}\). Finally, \(T(2^v)=2^{v-1}\) for all integers \(v\ge1\), so after exactly \(a+d\) further moves the orbit reaches \(1\). These three segments prove condition 1 and show the total number of moves is
\[
c+d+(a+d)=a+2b+(2h-1)c.
\]
There is exactly one legal move at every nonterminal position of the game. Starting at its terminal state \(1\) with Sprague–Grundy value \(0\), the value toggles between \(0\) and \(1\) on each preceding state. The initial value is therefore \(H(n)\bmod2=a+c\bmod2\), since \(2b\) is even and \(2h-1\) is odd. This proves the claims.

## Verification

The self-contained Python script `verify.py` performs integer-only trial-division totients and independently iterates the map to its terminal state. It checks the entire predicted orbit and height for \(120\) triples when \((q,h)=(13,3)\), and \(48\) triples when \((q,h)=(1093,7)\). For \(59\) other odd primes below \(300\), the script verifies that the first iterate from \(2\cdot3\cdot q\) acquires a prime factor outside the original support. Run `python3 verify.py`; the expected output is in `verification_output.txt`. These finite computations complement the unrestricted proof; they are not a proof of the universal quantifiers.

## Relationship to prior work

Ellis, Shi, Thanatipanonda, and Tu study the NONTOTIENT game and its cototient height in their 2023 paper, especially Section 4 and Theorem 4.2. Their theorem determines the height parity for a two-prime support when one prime is of the form \(p^h-p+1\); it does not state or classify cototient trajectories on the three-prime support \(\{2,3,q\}\). The present result gives a sharp support-closure criterion and an exact height for every exponent triple in precisely the closed three-prime cases.

Iannucci and Larsson introduced the arithmetic-function games and investigated prime powers and selected two-prime starting values, leaving broader cototient classifications open (Section 3.1.2 of their 2021 work). Their different TOTIENT game's classification is not applicable to the NONTOTIENT map. The theorem here does not claim that the existence of ternary-repunit primes is new.

## Limitations

There is no claim that infinitely many eligible distinct primes \(q\) exist; the infinite family is obtained by allowing the exponents to vary for each known eligible prime. The result does not classify the heights for supports that leak new prime factors, nor for starts lacking a factor \(2\) or \(3\). An equivalent unpublished or unindexed formulation cannot be excluded solely by searches. The stated proof does not require any computational or probabilistic assumption.

## References

1. P. Ellis, J. Shi, T. A. Thanatipanonda, A. Tu, “Two Games on Arithmetic Functions: SALIQUANT and NONTOTIENT,” arXiv:2309.01231v1, September 3, 2023, Section 4. https://arxiv.org/pdf/2309.01231
2. D. E. Iannucci and U. Larsson, “Game Values of Arithmetic Functions,” *Integers* 21B (2021), article A14, Section 3.1.2. https://math.colgate.edu/~integers/vb14/vb14.pdf
