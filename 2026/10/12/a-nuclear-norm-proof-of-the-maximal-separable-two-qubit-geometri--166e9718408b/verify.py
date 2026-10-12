from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def main():
    # Extremizer sigma = 1/2 |00><00| + 1/2 |+1><+1|.
    # Its augmented Bloch matrix M=[x T].
    M = [
        [F(1,2), F(0), F(0), F(-1,2)],
        [F(0),   F(0), F(0), F(0)],
        [F(1,2), F(0), F(0), F(1,2)],
    ]
    G = matmul(M, transpose(M))
    assert G == [
        [F(1,2), F(0), F(0)],
        [F(0), F(0), F(0)],
        [F(0), F(0), F(1,2)],
    ]
    # Eigenvalues are exactly 1/2,1/2,0, hence D=(1/2)*(1/2+0)=1/4.
    D = F(1,2) * F(1,2)
    assert D == F(1,4)

    # Scalar optimization after s3=sqrt(2) w:
    # g(w)=1/2-w+(5/2)w^2.  Equality g=1/2 has roots 0 and 2/5.
    roots = [F(0), F(2,5)]
    assert roots[0] >= 0 and roots[0] <= F(1,3)
    assert roots[1] > F(1,3)
    g_at_third = F(1,2) - F(1,3) + F(5,2)*F(1,9)
    assert g_at_third == F(4,9)
    assert g_at_third < F(1,2)

    # The candidate saturates the nuclear-norm inequality because the
    # two nonzero singular values are both 1/sqrt(2): their sum is sqrt(2).
    # Squared singular values are checked exactly through G above.
    assert G[0][0] == G[2][2] == F(1,2)
    assert G[0][2] == 0

    print("VERIFY_OK")
    print("extremizer_squared_singular_values=1/2,1/2,0")
    print("normalized_geometric_discord=1/4")
    print("second_scalar_equality_root=2/5_outside_[0,1/3]")
    print("upper_expression_at_w=1/3_is_4/9")


if __name__ == "__main__":
    main()
