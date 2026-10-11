# Unit-separation angle moduli of the affine-regular decagon
## Finding
Put
\[
r=\frac{\sqrt5-1}{2},\qquad \phi=1+r=\frac{1+\sqrt5}{2},\qquad r^2=1-r.
\]
Let
\[
N_{10}(s,t)=\max\{|s+t|,|rs+t|,r|t|,r|s|,|s+rt|\}.
\]
For every \(x,y\in S_{X_{10}}\) with \(N_{10}(x-y)=1\),
\[
\boxed{\frac{9-\sqrt5}{4}\le N_{10}(x+y)\le4-\sqrt5}.
\]
Therefore
\[
\boxed{\rho^a_{X_{10}}(1)=\frac{9\sqrt5-27}{16}},\qquad
\boxed{\delta^a_{X_{10}}(1)=\frac{8\sqrt5-19}{2}}.
\]
## Assumptions and scope
All scalars are real. The unit ball is the affine-regular decagon with consecutive vertices
\[
(1,0),(0,1),(-1,\phi),(-\phi,\phi),(-\phi,1)
\]
and their negatives. The maps
\[
R(s,t)=(-t,s+\phi t),\qquad S(s,t)=(t,s)
\]
are isometries, so the first unit vector may be reduced to
\[
x=(a,1-a),\qquad0\le a\le1.
\]
The angle moduli are
\[
\rho_X^a(\epsilon)=\sup_{\substack{x,y\in S_X\\\|x-y\|=\epsilon}}\left(1-\frac{\|x+y\|^2}{2}\right)
\]
and
\[
\delta_X^a(\epsilon)=\inf_{\substack{x,y\in S_X\\\|x-y\|=\epsilon}}\left(1-\frac{\|x+y\|^2}{2}\right).
\]
## Proof
Fix \(x=(a,1-a)\) and put \(z=x-y\). Then \(x,y,z\) are all unit vectors. Solving the intersections
\[
z\in S_{X_{10}}\cap(x-S_{X_{10}})
\]
for every pair of decagon edges gives, up to exchanging \(y\) and \(z\), exactly three branches:
\[
y=(2-r+ra,-r-a),\qquad0\le a\le r^2,
\]
\[
y=(\phi,-a-r),\qquad r^2\le a\le r,
\]
and
\[
y=(\phi,-1-r^2a),\qquad r\le a\le1.
\]
The exchanged solutions give the remaining three intersections; reflection by \(S\) maps their sum-norm formulas to the same formulas below after \(a\mapsto1-a\).

Set
\[
M=3-2r=4-\sqrt5.
\]
On the first branch, direct evaluation of the five defining functionals gives
\[
N_{10}(x+y)=\max\{M-r^2a,\phi+r^2a\}.
\]
The two affine terms meet at \(a=r^2/2\), yielding
\[
\min N_{10}(x+y)=\frac{M+\phi}{2}=2-\frac r2=\frac{9-\sqrt5}{4}.
\]
At either endpoint the value is \(M\).

On the second branch,
\[
N_{10}(x+y)=3r+(1-2r)a,
\]
whose range is
\[
3\sqrt5-5\le N_{10}(x+y)\le M.
\]
On the third branch,
\[
N_{10}(x+y)=\phi+(2-3r)a,
\]
with the same range. Moreover
\[
3\sqrt5-5-\frac{9-\sqrt5}{4}=\frac{13\sqrt5-29}{4}>0.
\]
Thus the global lower endpoint is the first-branch crossing and the global upper endpoint is \(M\).

For the lower endpoint take
\[
x=\left(\frac{3-\sqrt5}{4},\frac{1+\sqrt5}{4}\right),\qquad
y=\left(\frac32,-\frac{1+\sqrt5}{4}\right).
\]
Then \(N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1\) and
\[
x+y=\left(\frac{9-\sqrt5}{4},0\right).
\]
For the upper endpoint take
\[
x=(0,1),\qquad y=\left(\frac{5-\sqrt5}{2},-\frac{\sqrt5-1}{2}\right),
\]
for which the same three unit constraints hold and \(N_{10}(x+y)=4-\sqrt5\).

Since \(s\mapsto1-s^2/2\) is decreasing on \([0,\infty)\), the two displayed angle-modulus formulas follow.
## Verification
The branch list comes from solving \(x=z+y\) for all edge pairs and retaining exactly the parameter intervals on which both edge parameters lie in \([0,1]\). The bundled `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt5)\) to check the decagon vertices, symmetry generators, all three branch families, exchanged companions, and the two equality witnesses. Finite sampling is supplementary; exhaustive coverage is supplied by the analytic edge-intersection classification above.
## Relationship to prior work
Du, Ahmad, Din and Li introduced \(\delta_X^a(\epsilon)\) and \(\rho_X^a(\epsilon)\) in 2022, developed equivalent forms and geometric consequences, and computed selected classical examples. The inspected full text contains no affine-regular-decagon calculation.

The closest indexed exact result for the same invariant is the unit-separation smoothness value for the regular octagonal plane. It concerns a different norm and does not imply the decagonal edge classification. A separate indexed decagonal result computes a Banach--Mazur distance from a parallelogram, an affine-containment invariant that does not constrain unit pairs at norm distance one.

Exact searches for the modulus notation, the regular-decagon aliases, the two radical values, and the equivalent minimum/maximum chord statements found no covering result.
## Limitations
Only the unit-separation point \(\epsilon=1\) is determined. No complete \(\epsilon\)-profile is claimed. The proof uses the finite edge structure of the affine-regular decagon and does not assert an analogous formula for every regular polygon. Bibliographic and semantic searches cannot prove absolute novelty.
## References
1. D. Du, A. Ahmad, A. Din and Y. Li, “Some Moduli of Angles in Banach Spaces,” *Mathematics* 10 (2022), 2965, doi:10.3390/math10162965. Published 17 August 2022. MSC 46B20.
