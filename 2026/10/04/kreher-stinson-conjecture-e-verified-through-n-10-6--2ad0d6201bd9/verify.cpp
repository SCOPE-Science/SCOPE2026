#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

static const int W = 39;
static const int R = 12;
static const int N = 1000000;

ull pow3(int e) {
    __uint128_t x = 1;
    for (int i = 0; i < e; ++i) x *= 3;
    return (ull)x;
}

int ternary_digits(ull x) {
    int d = 0;
    do { ++d; x /= 3; } while (x);
    return d;
}

ull reverse_ternary_block(ull x, int r) {
    ull y = 0;
    for (int i = 0; i < r; ++i) {
        y = 3 * y + (x % 3);
        x /= 3;
    }
    return y;
}

bool full_palindrome(const vector<ull>& chunks, ull B) {
    vector<unsigned char> digits;
    digits.reserve((chunks.size() - 1) * W + ternary_digits(chunks.back()));
    for (size_t j = 0; j < chunks.size(); ++j) {
        ull x = chunks[j];
        int limit = (j + 1 < chunks.size()) ? W : ternary_digits(x);
        for (int i = 0; i < limit; ++i) {
            digits.push_back((unsigned char)(x % 3));
            x /= 3;
        }
    }
    for (size_t i = 0, j = digits.size() - 1; i < j; ++i, --j) {
        if (digits[i] != digits[j]) return false;
    }
    return true;
}

int main() {
    const ull B = pow3(W);
    const ull P3R = pow3(R);
    vector<ull> chunks(1, 1);
    vector<int> hits;
    vector<int> candidates;

    for (int n = 1; n <= N; ++n) {
        ull carry = 0;
        for (size_t i = 0; i < chunks.size(); ++i) {
            __uint128_t z = (__uint128_t)chunks[i] * 2 + carry;
            chunks[i] = (ull)(z % B);
            carry = (ull)(z / B);
        }
        if (carry) chunks.push_back(carry);

        ull top = chunks.back();
        int dt = ternary_digits(top);
        long long length = (long long)(chunks.size() - 1) * W + dt;

        if (length < 2 * R) {
            if (full_palindrome(chunks, B)) hits.push_back(n);
            continue;
        }

        ull low = chunks[0] % P3R;
        ull reversed_low = reverse_ternary_block(low, R);
        ull leading;

        if (dt >= R) {
            leading = top / pow3(dt - R);
        } else {
            __uint128_t joined = (__uint128_t)top * B + chunks[chunks.size() - 2];
            ull denominator = pow3(dt + W - R);
            leading = (ull)(joined / denominator);
        }

        if (leading == reversed_low) {
            candidates.push_back(n);
            if (full_palindrome(chunks, B)) hits.push_back(n);
        }
    }

    const vector<int> expected_hits = {1, 2, 3, 4};
    const vector<int> expected_candidates = {
        41298, 41299, 41300, 62318, 377166, 877495, 918265
    };

    assert(hits == expected_hits);
    assert(candidates == expected_candidates);
    cout << "VERIFY_OK\n";
    return 0;
}
