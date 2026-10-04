# A literal-definition reset-word obstruction in the \(E_n\) family
## Finding
In arXiv:1302.5793v2, the displayed definition of the automata \(E_n\) assigns
\[
\delta(i,b)=\begin{cases}i+1,&i<n,\\1,&i=n,\end{cases}
\]
so \(b\) is the full \(n\)-cycle. The same page states that the reset threshold is \(n^2-3n+2\). Read literally, these two statements are incompatible for every integer \(n\ge 5\).

Indeed, define
\[
r=\left\lfloor\frac{n-2}{2}\right\rfloor,
\qquad
w_n=(a^2b^{n-2})^r a^2.
\]
For the displayed transition formula, \(w_n\) resets every state to state \(3\). Its length is
\[
|w_n|=nr+2=n\left\lfloor\frac{n-2}{2}\right\rfloor+2,
\]
which is strictly below \(n^2-3n+2\) for every \(n\ge5\).

The discrepancy is internal to the public preprint: Figure 6 depicts a different \(b\)-action in which states \(1\) and \(2\) both go to \(3\), and the proof uses identities compatible with that figure but not with the displayed cyclic formula. Thus the result here is a reproducibility correction to the literal displayed definition, not a refutation of the theorem for the intended Figure-6 automaton.

## Assumptions and scope
Let \(n\ge4\), let the state set be \(Q_n=\{1,2,\ldots,n\}\), and interpret the displayed formulas in arXiv:1302.5793v2 literally:
\[
\delta(i,a)=\begin{cases}2,&i=1,\\3,&i=2,\\i,&i>2,\end{cases}
\qquad
\delta(i,b)=\begin{cases}i+1,&i<n,\\1,&i=n.\end{cases}
\]
The claim concerns only this literal transition table. It does not claim an exact reset threshold for that literal automaton, and it does not alter the reset-threshold statement for the different automaton drawn in Figure 6.

## Proof
Write \(B=a^2b^{n-2}\). Under the literal table, \(a^2\) maps the full state set to \(\{3,4,\ldots,n\}\). Since \(b\) is the full cycle, \(b^{n-2}\) shifts every state two positions backward cyclically, hence
\[
Q_n B=\{1,2,\ldots,n-2\}.
\]
More generally, whenever \(4\le m\le n-2\),
\[
\{1,2,\ldots,m\}a^2=\{3,4,\ldots,m\},
\]
and therefore
\[
\{1,2,\ldots,m\}B=\{1,2,\ldots,m-2\}.
\]
Inducting over the \(r=\lfloor(n-2)/2\rfloor\) copies of \(B\), the image of \(Q_n\) is \(\{1,2\}\) when \(n\) is even and \(\{1,2,3\}\) when \(n\) is odd. A final \(a^2\) sends either set to \(\{3\}\). Hence \(w_n=B^r a^2\) is a reset word.

Each copy of \(B\) has length \(n\), so \(|w_n|=nr+2\). If \(n\) is odd then
\[
(n^2-3n+2)-|w_n|=\frac{n(n-3)}2>0,
\]
and if \(n\) is even then
\[
(n^2-3n+2)-|w_n|=\frac{n(n-4)}2>0
\]
for \(n\ge6\). The remaining case \(n=5\) is covered by the odd formula. Therefore the literal table has a reset word strictly shorter than the threshold stated in Theorem 4 for every \(n\ge5\).

There is a second independent consistency check. The proof of Theorem 4 states that the words \(bab\) and \(b^2\) act identically. Under the displayed cyclic \(b\), state \(1\) is sent by \(bab\) to state \(4\) but by \(b^2\) to state \(3\), for \(n\ge4\). Figure 6 instead depicts the non-cyclic \(b\)-action used by the proof.

## Verification
The accompanying `artifacts/verify.py` constructs the literal automaton directly from the displayed transition formulas. It replays \(w_n\), checks its stated length and strict inequality for \(4\le n\le12\), and independently computes exact reset thresholds by breadth-first search in the full power automaton for these values. It also stress-tests the symbolic endpoint recurrence through \(n=500\). The recorded output ends with `VERIFY_OK symbolic_n_max=500 exhaustive_power_n_max=12`.

The finite calculations are verification only. The universal statement for every \(n\ge5\) is established by the interval-image argument above.

## Relationship to prior work
The 2013 paper introduces the \(E_n\) family and states Theorem 4. Its displayed transition table on the page preceding the proof makes \(b\) cyclic, while Figure 6 and the proof encode a different action. The 2010 conference precursor announces that an additional family with reset length \(n^2-3n+2\) would appear in an extended version, but it does not define \(E_n\); it therefore does not resolve the displayed-definition discrepancy.

Targeted searches for the family name, the theorem value, the identities \(bab=b^2\), and erratum/correction terminology did not locate a published statement of this literal-table obstruction. A later literature snippet uses a relabeled description of an \(E_n\) family but does not supply or analyze this discrepancy. The main residual originality risk is an informal or non-indexed correction of the printed transition table.

## Limitations
This finding does not determine the exact reset threshold of the literal cyclic-table automaton for all \(n\), although the verifier reports exact small-state thresholds as stress data. It does not claim that the intended Figure-6 automaton violates Theorem 4. It is confined to the public arXiv v2 presentation and its internal consistency; a separately typeset journal copy was not used to broaden the claim.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Primitive digraphs with large exponents and slowly synchronizing automata*, arXiv:1302.5793v2; DOI:10.1007/s10958-013-1392-8. See the displayed definition of \(E_n\), Figure 6, and Theorem 4 with its proof on pp. 12–13 of the arXiv PDF.
2. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Slowly Synchronizing Automata and Digraphs*, MFCS 2010, DOI:10.1007/978-3-642-15155-2_7. The conference version announces the additional \(n^2-3n+2\) family without defining \(E_n\).
