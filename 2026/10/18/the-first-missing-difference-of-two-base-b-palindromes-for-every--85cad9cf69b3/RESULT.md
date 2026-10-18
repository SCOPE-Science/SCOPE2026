# The first missing difference of two base-\(b\) palindromes for every base \(b\ge5\)

## Finding

Let \(\mathcal P_b\) be the positive base-\(b\) palindromes and \(\mathcal D_b=\{v-u: v,u\in\mathcal P_b,\ v>u\}\). For every integer \(b\ge5\),
\[
\min(\mathbb Z_{>0}\setminus\mathcal D_b)=b^3-(b-1)^2.
\]
In digits, the first missing difference is \(((b-1)1(b-1))_b\). For example, it is \(109\) in base \(5\), \(191\) in base \(6\), and \(919\) in base \(10\). The theorem concerns differences of arbitrary positive palindromes, not only consecutive palindromes.

## Assumptions and scope

All digits are ordinary, with no leading zero. Here \(b\) is an integer \(\ge5\). For \(1\le a\le b-1\) and \(0\le c\le b-1\), write \(J_a=a(b+1)=(aa)_b\) and \(P_{a,c}=a(b^2+1)+cb=(aca)_b\). Define \(U=(111)_b=b^2+b+1\) and \(V=(1111)_b=b^3+b^2+b+1\), and put \(T=b^3-(b-1)^2=P_{b-1,1}\).

## Proof

**Every \(1\le d<T\) is attained.** For any base-\(b\) palindrome \(W\), the integers \(W-t\), \(1\le t\le b-1\), are differences of positive palindromes whenever \(W>t\). Using \(J_a\), this covers the intervals \([J_a-(b-1),J_a-1]\) for \(1\le a\le b-1\). The value \(1\) is \(2-1\). For each \(1\le a\le b-2\), the two values between consecutive intervals are supplied by
\[
J_a=J_{a+1}-J_1,\qquad J_a+1=U-J_{b-a}.
\]
Consequently all \(1\le d\le b^2-2\) are covered. The first three-digit interval, from \(P_{1,0}=b^2+1\), begins at \(b^2-b+2\) and ends at \(b^2\), so it joins without a gap for \(b\ge5\).

Next order the \(P_{a,c}\) lexicographically by \(a,c\). The associated intervals \([P_{a,c}-(b-1),P_{a,c}-1]\) cover all intervening values except possibly the right endpoint \(P_{a,c}\) for transitions \(c\to c+1\), and the two values \(P_{a,b-1}\), \(P_{a,b-1}+1\) for transitions \(a\to a+1\). Each such gap below \(T\) has an explicit representation:
\[
P_{a,c}=P_{b-1,c}-P_{b-1-a,0}\quad(1\le a\le b-2),
\]
\[
P_{a,b-1}+1=V-P_{b-a,1}\quad(1\le a\le b-2),
\]
and
\[
P_{b-1,0}=V-P_{2,0}.
\]
All displayed differences use positive palindromes with valid digits. To cover the final segment \([T-(b-1),T-1]\), use differences \(T-t\), \(1\le t\le b-1\). This proves \([1,T-1]\subseteq\mathcal D_b\). (The last interval is used to represent values below \(T\); it does not claim that \(T\) is a difference.)

**The value \(T\) cannot occur.** Suppose \(v-u=T\) with positive palindromes \(v>u\). We have \(b^2<T<b^3\) and \(T\equiv b-1\pmod b\). A quantitative consequence of the *proof* of Pongsriiam–Saito Theorem 12 is: if \(d\) has \(r+1\) base-\(b\) digits and two palindromes differ by \(d\), with the smaller at least \(b^{2r+1}\), then \(d=2\) or \(d=b^j+b^{j-1}\) for an allowable \(j\le r\). For \(r=2\) neither possibility equals \(T\), hence necessarily \(u<b^5\), and then \(v<b^5+b^3\) has at most six digits.

If \(u,v\) have the same digit length, their last-digit difference is the nonnegative leading-digit difference \(\le b-2\), contradicting \(T\equiv b-1\pmod b\). Two or fewer digits for \(v\) are impossible. If \(v\) has three digits and \(u\) at most two, its leading/last digit must be \(b-1\) because \(T\ge (b-1)b^2\); subtracting \(T\) then forces \(u\equiv0\pmod b\), impossible for a positive one- or two-digit palindrome.

Suppose \(v\) has four digits and \(u\) has at most three. Necessarily \(v=(1BB1)_b\): a four-digit palindrome beginning at least \(2\) exceeds every three-digit palindrome by more than \(T\). If \(u\) has one digit, then \(v-u\ge b^3-b+2>T\). If \(u=(aa)_b\), reduction modulo \(b\) forces \(a=2\), and comparing the remaining coefficients forces \((B+1)b+B-4=0\), impossible for \(b\ge5\). If \(u=(aca)_b\), similarly \(a=2\), and comparison forces \((B-1)b+B-c-2=0\), impossible: it is negative for \(B\le1\) and positive for \(B\ge2\), using \(0\le c<b\).

If \(v\) has five digits and \(u\) at most four, \(u\) must have four digits: otherwise their difference exceeds \(b^3\). The bound \(T<b^3\) forces the leading digit of \(v\) to be \(1\) and of \(u\) to be \(b-1\); their last digits therefore give \(v-u\equiv 1-(b-1)\equiv2\pmod b\), contradicting \(T\equiv b-1\pmod b\) since \(b\ge5\). The same argument applies to six-digit \(v\) and five-digit \(u\): \(u<b^5\), the difference is less than \(b^3\), and hence the leading digits are \(1\) and \(b-1\), respectively. All lengths have been excluded, so \(T\notin\mathcal D_b\). \(\square\)

## Verification

`verify.py` independently evaluates constructive witnesses for every \(d<T\) in bases \(5\) through \(20\), and searches every positive palindrome below \(b^5\) for a forbidden difference \(T\) in bases \(5\) through \(10\). It does not substitute a finite search for the universal argument, which relies on the cited large-palindrome gap lemma. Execute `python3 verify.py`.

## Relationship to prior work

Pongsriiam and Saito classify those fixed positive differences realized by infinitely many pairs of base-\(b\) palindromes. Their Theorem 12 and its proof give the threshold reduction used here, and their Question 25 asks for properties of the full palindrome difference set. The present result computes the *least missing positive difference* uniformly for every \(b\ge5\), a different invariant not stated by that theorem. Base-specific first gaps, including the binary OEIS entry and decimal \(919\), do not imply the uniform formula without the coverage proof and the full-length exclusion.

## Limitations

The formula as stated does not include bases \(2\), \(3\), and \(4\); their first missing differences are different. It determines only the first omission, not the complete difference set, its density, or arithmetic progressions. The quoted quantitative reduction is taken from the published proof of Theorem 12 and must not be confused with deriving a bound merely from the theorem's infinitude statement. Independent mathematical auditing has not been performed.

## References

P. Pongsriiam and K. Saito, “Palindromes and Antipalindromes in Short Intervals,” Journal of Integer Sequences 26 (2023), Article 23.9.5, Theorem 12, its proof, and Question 25. https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.pdf ; published 2023-12-11: https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.html
OEIS A290393, first missing binary palindrome differences (different base, distinct first obstruction). https://oeis.org/A290393
