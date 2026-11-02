# An exact length-independent census of finite words below the Morse–Hedlund threshold

## Finding

Let \(\Sigma\) be a labeled alphabet with \(q\ge1\) symbols. For a word \(W\), let \(f_W(k)\) denote the number of distinct contiguous factors of length \(k\). For any integers \(k\ge1\) and \(L\ge2k\), put

\[
C_{q,k}(L)=\#\{W\in\Sigma^L:f_W(k)\le k\}.
\]

**Theorem (unique core and exact census).** Every word counted by \(C_{q,k}(L)\) has a unique representation

\[
W=u\,v^{[L-a-b]}\,z,\qquad a=|u|,\quad b=|z|,\quad p=|v|,
\]

in which \(p\ge1\), \(a+b+p\le k\), \(v\) is primitive (not a proper integer power), and \(v^{[m]}\) denotes the length-\(m\) prefix of the infinite periodic word \(vvvv\cdots\). If \(a>0\), the last letter of \(u\) differs from the letter immediately preceding the displayed periodic core in its unique periodic continuation; if \(b>0\), the first letter of \(z\) differs from the next letter of that continuation. Conversely, every such representation has \(f_W(k)\le k\).

Define

\[
M_q(p)=\sum_{d\mid p}\mu(d)q^{p/d},\qquad H_q(0)=1,
\]

and, for \(m\ge1\),

\[
H_q(m)=(m+1)q^m-mq^{m-1}.
\]

Then the exact answer, independent of \(L\) throughout \(L\ge2k\), is

\[
\boxed{C_{q,k}(L)=C_{q,k}=\sum_{p=1}^k M_q(p)H_q(k-p).}
\]

In particular,

\[
\sum_{k\ge1}C_{q,k}t^k=
\frac{1-t}{(1-qt)^2}\sum_{p\ge1}M_q(p)t^p,
\]

and for every fixed \(q\ge2\),

\[
C_{q,k}=\left(\frac{q-1}{2q}k^2+O_q(k)\right)q^k
\quad\text{as }k\to\infty.
\]

For example, \(C_{2,k}\) for \(1\le k\le9\) is
\(2,8,28,86,250,680,1792,4562,11344\); for any \(L\ge6\), exactly \(28\) binary words of length \(L\) have at most three different length-three factors. The bound \(L\ge2k\) is a uniform onset threshold; for \(L=2k-1\) the condition is vacuous, and for fixed \(k\ge2\) sufficiently large alphabets show that a smaller uniform threshold cannot hold.

## Assumptions and scope

All letters are labeled; words are linear rather than circular. The factor relation is contiguous, and the inequality is non-strict. The alphabet may consist of only one letter. The central periodic word is anchored at its first letter following the left fringe; no quotient by rotation or by letter relabeling is taken. The statements hold for all \(k\ge1\), all \(L\ge2k\), and all positive integral \(q\); the asymptotic statement fixes \(q\ge2\) and lets \(k\to\infty\). The finite Morse–Hedlund decomposition invoked below is from Khrystik [1, Theorem 3.5].

## Proof

**1. Existence of a periodic center.** Khrystik [1, Theorem 3.5] states that when \(L\ge2k\), \(f_W(k)\le k\) holds exactly when there are integers \(a,b\ge0\), \(p\ge1\), with \(a+p+b\le k\), such that the substring after the first \(a\) and before the last \(b\) letters is periodic with period \(p\). Replace \(p\) by the primitive period of this repetition. Extend its associated two-sided periodic sequence over matching adjacent letters to the left and to the right, stopping only at a word endpoint or a mismatch. This decreases \(a+b\), does not increase \(p\), and produces the required boundary-normal representation.

**2. Uniqueness of the normalized center.** Suppose two such representations have periods \(p,p'\) and fringe lengths \(a,b,a',b'\). Their periodic centers are the position intervals \([a,L-b)\) and \([a',L-b')\), whose overlap has length

\[
L-\max(a,a')-\max(b,b')
\ge L-(a+b+a'+b')\ge L-2k+p+p'\ge p+p'.
\]

Both periods apply to the overlap. By the Fine–Wilf periodicity theorem [2], the overlap has period \(d=\gcd(p,p')\). Since it contains at least \(p\) consecutive letters from a \(p\)-periodic word, its length-\(p\) segment would be a repetition of a length-\(d\) block if \(d<p\); that contradicts the primitivity of the first central period. Likewise \(d=p'\). Therefore \(p=p'=d\). Agreement on the overlap (at least \(p\) letters) makes the two bi-infinite periodic continuations equal with identical phase. If \(a<a'\), the last left-fringe letter in the second representation lies within the first periodic center, contradicting its required mismatch; similarly \(a'>a\) is impossible. Thus \(a=a'\), and the symmetric argument yields \(b=b'\). All displayed components are then identical.

**3. Sufficiency and counting.** The at most \(a\) length-\(k\) factors starting before the central core and the at most \(b\) factors ending after it contribute at most \(a+b\) distinct values. All remaining factors are inside a \(p\)-periodic substring and contribute at most \(p\). Thus \(f_W(k)\le a+p+b\le k\). The central substring is long enough for this argument: \(L-a-b\ge L-k+p\ge k+p\).

There are exactly \(M_q(p)\) primitive words of length \(p\), by the usual Möbius inversion of the formula \(q^p=\sum_{d\mid p}M_q(d)\). For a fixed primitive core, there are \(F_q(0)=1\) admissible left fringes of length zero, and for length \(a>0\) there are \(F_q(a)=(q-1)q^{a-1}\) choices: the last letter must disagree with the preceding periodic letter, and all earlier letters are unrestricted. The same count holds for a right fringe of length \(b\), whatever the phase at that endpoint. Uniqueness just proved prevents duplicate counting. Hence

\[
C_{q,k}=\sum_{p=1}^{k}M_q(p)
\sum_{a+b\le k-p}F_q(a)F_q(b).
\]

Now \(\sum_{a\ge0}F_q(a)t^a=(1-t)/(1-qt)\), so the generating function of the cumulative convolution is \((1-t)/(1-qt)^2\). Its coefficient of degree \(m\) is precisely \(H_q(m)\), proving both stated generating identities and independence from \(L\).

**4. Growth for large factor length.** For fixed \(q\ge2\), the nonprimitive length-\(p\) words number at most \(O_q(pq^{p/2})\). Thus \(M_q(p)=q^p+O_q(pq^{p/2})\). Inserting this into the exact convolution, using \(H_q(m)\le(m+1)q^m\), gives an overall error of \(O_q(kq^k)\). Replacing \(M_q(p)\) by \(q^p\), the main sum equals

\[
q^k\sum_{m=0}^{k-1}\bigl((m+1)-m/q\bigr)
=q^k\left(\frac{k(k+1)}2-\frac{k(k-1)}{2q}\right).
\]

This establishes the claimed asymptotic law. Finally, every length-\((2k-1)\) word has only \(k\) length-\(k\) factor positions and is therefore counted, while the exact count at \(2k\) has degree \(k\) in \(q\), versus \(q^{2k-1}\) at \(2k-1\); for \(k\ge2\) the onset is thus uniform-sharp over growing alphabets.

## Verification

The accompanying `verify.py` evaluates the Möbius formula, independently enumerates complete small word spaces, and separately constructs all primitive-boundary normal forms. `verify_output.txt` gives the actual reproducible output. Literal enumeration checked \(35\) alphabet/length/factor-size triples; duplicate-freeness, admissibility, and predicted cardinalities of normal forms were checked in \(47\) more parameter triples. All tests passed. These finite computations are corroboration; the unrestricted theorem rests on the structural argument above and the cited finite Morse–Hedlund theorem, not on finite enumeration.

## Relationship to prior work

Khrystik [1] supplies the necessary and sufficient **existence** of a bounded-fringe periodic decomposition for finite low-complexity words. Its Theorem 3.5 and the stronger Theorem 4.8 do not state a unique primitive normalized decomposition, an all-alphabet word count, length stabilization, or the primitive-word convolution. The new step is the simultaneous periodic-center overlap argument using Fine–Wilf, which establishes disjoint normal forms and enables exact enumeration. Anisiu and Cassaigne [3] analyze the shape and maxima of individual finite-word complexity functions rather than counting the entire low-complexity class. De Luca [4] studies special factors and finite-word structural parameters, but its complete text was not inspected; any prior enumerative treatment there remains a priority risk. None of these statements claims a new finite Morse–Hedlund existence theorem.

## Limitations

This theorem treats the threshold \(f_W(k)\le k\) and word lengths \(L\ge2k\), not the distribution at every complexity threshold or short-word lengths. It does not enumerate equivalence classes under word reversal, alphabet permutations, or cyclic rotation. Its novelty assessment is literature-based, not a guarantee of global publication priority. The structural input [1] and classical Fine–Wilf theorem [2] are explicitly credited.

## References

[1] M. A. Khrystik, *Combinatorics on finite words and the length of a finite-dimensional associative algebra*, first posted 30 April 2026, arXiv:2605.00141, Theorems 3.5 and 4.8. https://arxiv.org/abs/2605.00141

[2] N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proceedings of the American Mathematical Society 16 (1965), 109–114. https://doi.org/10.1090/S0002-9939-1965-0174934-9

[3] M.-C. Anisiu and J. Cassaigne, *Properties of the complexity function for finite words*, Revue d'analyse numérique et de théorie de l'approximation 33 (2004), 123–139. https://ictp.acad.ro/properties-of-the-complexity-function-for-finite-words/

[4] A. de Luca, *On the combinatorics of finite words*, Theoretical Computer Science 218 (1999), 13–39. https://doi.org/10.1016/S0304-3975(98)00248-5
